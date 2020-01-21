"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import BlogListViews,TagListViews,blog_detail

app_name= "main"

urlpatterns = [
   path('',BlogListViews.as_view(),name='blog-homepage'),
   path('about/',views.about,name='blog-about'),
   #path('blog/<int:pk>/',BlogDetailViews.as_view(),name='blog_detail'),
   #path of class based view is removed from the url patterns, also detailview.html page is reshaped into detail.html file.
   path('blog/tagged/<slug:slug>/',TagListViews.as_view(),name='tagged_blogs'),
   path('blog/tagged/book/',TagListViews.as_view(),name='book_blog'),
   path('blog/<int:id>/',blog_detail,name='blog_page'),
   path('blog/latestprojects/',views.latestproj,name='latest_proj'),

]
