from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=400,verbose_name='Blog Title')
    content=RichTextUploadingField(verbose_name='Blog Content')
    date_posted=models.DateTimeField(default=timezone.now,verbose_name='Published Date')
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    tags=TaggableManager(verbose_name='tags',help_text='Use comma seperated names for separate tags')
   
    def __str__(self):
        return self.title


