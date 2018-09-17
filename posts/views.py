from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

def post_create(request):
    return HttpResponse("Create")

def post_detail(request):
    instance = get_object_or_404(Post, id=1)
    context = {
        "title": "Detail",
        "instance": instance
    }
    return render(request, "detail.html", context)

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

