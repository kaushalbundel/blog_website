from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Blog
from taggit.models import Tag
from django.shortcuts import get_object_or_404
from django.db.models import Count

#creating views using class based views

class BlogListViews(ListView):
    model=Blog
    template_name='main/home.html' #class based view require template as well <app name>/<model name>_<viewtype>.html
    ordering=['-date_posted'] # We have made a slight change in the template also, where the for loop as been changed (ref: object list)
#CBV is removed from the code    
#class BlogDetailViews(DetailView):
    #model=Blog
    #template_name='main/detailview.html'

class TagListViews(ListView):
    """This is used for having a list view for tags that we have added using taggit in models"""
    model=Blog
    template_name='main/home.html'

    def get_queryset(self):
        return Blog.objects.filter(tags__slug=self.kwargs.get("slug")).all()
    class meta:
        ordering = ['-date_posted']
    def get_context_data(self, **kwargs):
        context=super(TagListViews,self).get_context_data(**kwargs)
        context["tag"]=self.kwargs.get("slug")
        return context
    
    
#defining about page 
def about(request):
    return render(request,'main/about.html',{'title':'About'})

#blog detail page is remade. Earlier CBV were being used and now function based views is used to sort out the problem with similar pages
def blog_detail(request,id):
    blog=get_object_or_404(Blog,id=id)
    tags = blog.tags.all()
    similar_blog = Blog.objects.filter(tags__in=tags).exclude(id=blog.id)
    return render(request, 'main/detail.html', {'blog': blog, 'similar_blog': similar_blog})

#defining latest project page
def latestproj(request):
    return render(request,'main/latestprojects.html',{'title':latestproj})

