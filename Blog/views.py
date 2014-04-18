from django.shortcuts import render, render_to_response , get_object_or_404 # sonra kullanilmayan importlari silebilirim
from Blog.models import *

def blog_index(request):
    data = {
        'title' : 'Welcome to My Blog!',
        'categories': Category.objects.all(),
        'posts': Post.objects.filter(isEnabled=True)[:5]
    }
    return render_to_response("index.html",data)


def blog_post(request, slug):
    pass


def blog_search(request, query):
    #TODO: Add a search query and return the result.
    pass