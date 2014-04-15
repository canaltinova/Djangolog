from django.core.validators import validate_slug

class Post(models.Model):
    #defining fields for Post model
    title = models.CharField(max_length=100,verbose_name='Başlık')
    slug = models.SlugField(unique=true)
    content = models.TextField(verbose_name='İçerik')
    author = models.ForeignKey(User,verbose_name='Yazar')
    date = models.DateTimeField(auto_now_add=True,verbose_name="Yayınlanma Tarihi")
    tags = models.ManyToManyField(tag)
    viewCount = models.IntegerField(default=0,verbose_name='Görülme Sayısı')
    lastEdit = models.DateTimeField(verbose_name="Son Güncelleme")
    isEnabled = models.NullBooleanField(blank=True, default=0, verbose_name='Enabled')
    
    
    def __unicode__(self):
        return self.slug
    
    
    
class Tag(models.Model):
    text = models.CharField(max_length=15, unique=True, validators=[validate_slug])

    def __unicode__(self):
        return self.yazi
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=true)
    
    def __unicode__(self):
        return self.slug
    
class Page(models.Model):
    titile = models.CharField(Max_length=50, verbose_name='Başlık')
    slug = models.SlugField(unique=true)
    content = models.TextField(verbose_name='İçerik')
    