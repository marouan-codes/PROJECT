from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse

# Create your models here.
class portfolo(models.Model):
    slug= models.SlugField(blank=True)
    h1_tag= models.CharField(max_length=150)
    title= models.CharField(max_length=150)
    description=models.CharField(max_length=200)
    duree= models.CharField(max_length=40)
    designtool= models.ImageField(upload_to="static/images")
    devtool= models.ImageField(upload_to="static/images")
    siteimages= models.ImageField(upload_to="static/images")
    profileimage= models.ImageField(upload_to="static/images", blank=True)
    text_info=CKEditor5Field(max_length=3000)
    website= models.URLField(max_length=100, blank=True)
    loom_video = models.URLField(blank=True)
    last_modified= models.DateField(default='2022-01-01')
    
    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse('portfoliopage', args=[self.slug])
    

class blog(models.Model):
    slug= models.SlugField(blank=True)
    h1_title= models.CharField(max_length=150)
    tag= models.CharField(max_length=50, blank=True)
    meta_description=models.CharField(max_length=200)
    published=models.CharField(max_length=90)
    blogimage= models.ImageField(upload_to="static/images")
    content= CKEditor5Field(max_length=5000, blank=True)
    author= models.CharField(max_length=90, default='Marouan Kaboul')
    last_modified= models.DateField(default='2022-01-01')
    
    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse('blogpage', args=[self.slug])
    
class adawat(models.Model):
    website= models.URLField(blank=True)
    h1_title= models.CharField(max_length=150)
    tag= models.CharField(max_length=50, blank=True)
    meta_description=models.CharField(max_length=200)
    adatimage= models.ImageField(upload_to="static/images")

    def __str__(self):
        return self.h1_title

    
    
# @property
# def structured_data(self):
        
#         data = {
#             "@context": "https://schema.org",
#             "@type": "BlogPosting",
#             "headline": self.h1_title,
#             "description": self.meta_description,
#             "datePublished": self.published,
#             "image": self.blogimage.url if self.blogimage else None,
#             "url": self.get_absolute_url(),
#             "author": {
#                 "@type": "Person",
#                 "name": self.author
#             }
#         }
#         return data

# def get_absolute_url(self):
#     return reverse('blog-detail', args=[str(self.slug)])


