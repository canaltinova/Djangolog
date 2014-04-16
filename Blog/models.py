from django.db import models
from django.core.validators import validate_slug

#defining fields for models

#TODO: user is nod defined right now it should work later(in post and page)
class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='Baslik')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Icerik')
    #author = models.ForeignKey(User,verbose_name='Yazar')
    date = models.DateTimeField(auto_now_add=True,verbose_name="Yayinlanma Tarihi")
    # todo: tags = models.ManyToManyField(tag)
    imagePath = models.TextField(verbose_name='Resim Yolu')
    viewCount = models.IntegerField(default=0,verbose_name='Gorulme Sayisi')
    lastEdit = models.DateTimeField(verbose_name="Son Guncelleme")
    isEnabled = models.NullBooleanField(blank=True, default=0, verbose_name='Enabled')
    
    
    def __unicode__(self):
        return self.slug
    
    
    
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
    titile = models.CharField(max_length=50, verbose_name='Baslik')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Icerik')
    #author = models.ForeignKey(User,verbose_name='Yazar')
    viewCount = models.IntegerField(default=0,verbose_name='Gorulme Sayisi')
    lastEdit = models.DateTimeField(verbose_name="Son Guncelleme")
    isEnabled = models.NullBooleanField(blank=True, default=0, verbose_name='Enabled')
    
    def __unicode__(self):
        return self.slug

class Site(models.Model):
    title =  models.CharField(max_length=50)
    value = models.TextField()
    description = models.TextField()
    
    def __unicode__(self):
        return self.title