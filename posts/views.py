from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # Message Create
        return HttpResponseRedirect(instance.get_absolute_url())
        #   print form.cleaned_date.get("title")
    # if request.method == "POST":
        # print "title" + request.POST.get("content")
        # print request.POST.get("title")
        # Post.objects.create(title=title)
    context = {
    "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
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

def post_update(request, id=id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
    "title": instance.title,
    "instance": instance,
    "form": form
    }
    return render(request, "post_form.html", context)

def post_delete(request):
    return HttpResponse("Delete")

