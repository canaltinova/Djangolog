from django.shortcuts import render, render_to_response

def blog_index(request):
    data = {
        'title' : 'Welcome to My Blog!'
    }
    return render_to_response("index.html",data)


def blog_search(request, query):
    #TODO: Add a search query and return the result.
    pass


def blog_content(request, slug):
    #TODO: Add a query to select the current post.
    pass