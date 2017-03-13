from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog, Post


class BlogList(ListView):

    queryset = Blog.objects.all()
    template_name = 'blogs/blog_list.html'


class BlogView(DetailView):

    queryset = Blog.objects.all()
    template_name = 'blogs/blog.html'


class PostView(DetailView):

    queryset = Post.objects.all()
    template_name = 'blogs/post.html'
