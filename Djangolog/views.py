from django.shortcuts import render_to_response

def anasayfaView(request):
    data = {
        'title' : 'Welcome to My Blog!'
    }
    return render_to_response("blog_index.html",data)