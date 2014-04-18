from django.db import models
from django.core.validators import validate_slug
from django.contrib.auth.models import User

#defining fields for models

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='Baslik')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Icerik')
    author = models.ForeignKey(User,verbose_name='Yazar')
    created = models.DateTimeField(auto_now_add=True,verbose_name="Yayinlanma Tarihi")
    #tags = models.ManyToManyField('Blog.Tag')
    imagePath = models.CharField(max_length=500,verbose_name='Resim Yolu')
    viewCount = models.IntegerField(default=0,verbose_name='Gorulme Sayisi')
    lastEdit = models.DateTimeField(verbose_name="Son Guncelleme")
    isEnabled = models.BooleanField(default=True, verbose_name='Enabled')
    category = models.ForeignKey('Blog.Category')
    
    class Meta:
            ordering = ['-created']
    
    def __unicode__(self):
        return self.slug
    
    def get_absolute_url(self):
            return reverse('Blog.views.Post', args=[self.slug])
        
    def get_content_description(self):
        if len(self.content) >= 250:
            return self.content[:250]
        else:
            return self.content
        
    def get_image(self):
        if len(self.imagePath) >0:
            return self.imagePath
        else:
            return 'resimyok.png'
    
    
    
class Tag(models.Model):
    text = models.CharField(max_length=15, unique=True, validators=[validate_slug])

    def __unicode__(self):
        return self.text
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.slug
    
    
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name='Baslik')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Icerik')
    author = models.ForeignKey(User,verbose_name='Yazar')
    viewCount = models.IntegerField(default=0,verbose_name='Gorulme Sayisi')
    lastEdit = models.DateTimeField(verbose_name="Son Guncelleme")
    isEnabled = models.BooleanField(default=True, verbose_name='Enabled')
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=True)
    
    #class Meta:
    #        ordering = ['-lastEdit'] bir index degiskeni olusturup onun uzerinde bir siralama yapabilirim. simdilik boyle kalsin.
            
    def __unicode__(self):
        return self.slug
    
    def get_absolute_url(self):
            return reverse('Blog.views.Post', args=[self.slug])

class Comment(models.Model):
    title = models.CharField(max_length=50, verbose_name='Baslik')
    content = models.TextField(verbose_name='Icerik')
    post = models.ForeignKey('Blog.Post')
    sender = models.CharField(max_length=50, verbose_name='Gonderen')
    isEnabled = models.BooleanField(default=False, verbose_name='Enabled')
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=True)
    
    
    
class SiteSetting(models.Model):
    title =  models.CharField(max_length=50)
    value = models.TextField()
    description = models.TextField()
    
    def __unicode__(self):
        return self.title