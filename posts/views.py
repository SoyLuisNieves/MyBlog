from urllib import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    # if not request.user.is_authenticated():
    #    raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # Message Create
        messages.success(request, "Successfully created")
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

def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)
    context = {
        "title": "Detail",
        "instance": instance,
        "share_string": share_string,
    }
    return render(request, "detail.html", context)

def post_list(request):

    queryset_list = Post.objects.all()# .order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)
            ).distinct()
    paginator = Paginator(queryset_list, 10)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
        
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
    }
    
#    if request.user.is_authenticated():
#        context = {
#            "title": "My user list"
#        }
#    else:
#        context = {
#            "title": "List"
#        }
        
    return render(request, "post_list.html", context)

def post_update(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#''>Item Saved</a>", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
    "title": instance.title,
    "instance": instance,
    "form": form
    }
    return render(request, "post_form.html", context)

def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Sucessfully deleted")
    return redirect("posts:list")

