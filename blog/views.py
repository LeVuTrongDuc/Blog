from django.shortcuts import render
from .models import Post
# # Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm, BlogPostForm
from .models import *


@login_required(login_url = '/login')
def add_blogs(request):
    if request.method=="POST":
        forms = BlogPostForm(data=request.POST, files=request.FILES)
        if forms.is_valid():
            blogpost = forms.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = forms.instance
            alert = True
            return render(request, "blog/add_blog.html",{'obj':obj, 'alert':alert})
    else:
        forms=BlogPostForm()
    return render(request, "blog/add_blog.html", {'form':forms})




