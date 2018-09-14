from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

def post_create(request):
    return HttpResponse("Create")

def post_detail(request):
    context = {
        "title": "Detail"
    }
    return render(request, "index.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    
#    if request.user.is_authenticated():
#        context = {
#            "title": "My user list"
#        }
#    else:
#        context = {
#            "title": "List"
#        }
        
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("Update")

def post_delete(request):
    return HttpResponse("Delete")

