from django.contrib import admin
from Blog.models import Post, Category, Page
    
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'created']
    # fields to filter the change list with
    list_filter = ['isEnabled', 'created']
    # fields to search in change list
    search_fields = ['title', 'content']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}

class PageAdmin(admin.ModelAdmin):
    exclude = ['created']
    # fields display on change list
    list_display = ['title', 'created']
    # fields to filter the change list with
    list_filter = ['isEnabled', 'created']
    # fields to search in change list
    search_fields = ['title', 'content']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(Page,PageAdmin)