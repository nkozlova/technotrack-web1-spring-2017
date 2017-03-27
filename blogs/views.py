# coding: utf-8
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Blog, Post, Category
from django import forms


class SortForm(forms.Form):

    sort = forms.ChoiceField(choices={
        ('title', u'Заголовок'),
        ('description', u'Описание'),
    },
        widget=forms.RadioSelect
    )
    search = forms.CharField(required=False, widget=forms.TextInput)


class UpdateBlog(UpdateView):

    template_name = 'blogs/edit_blog.html'
    model = Blog
    fields = ('title', 'description', 'category')
    success_url = '/blogs/'

    def dispatch(self, request, *args, **kwargs):
        self.success_url += kwargs['pk']
        return super(UpdateBlog, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)


class CreateBlog(CreateView):

    template_name = 'blogs/add_blog.html'
    model = Blog
    fields = ('title', 'description', 'category')
    success_url = '/blogs/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlog, self).form_valid(form)


class BlogList(ListView):

    queryset = Blog.objects.all()
    template_name = 'blogs/blog_list.html'
    sortform = None

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context

    def get_queryset(self):
        qs = super(BlogList, self).get_queryset()
        if self.sortform.is_valid():
            qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs


class BlogView(DetailView):

    queryset = Blog.objects.all()
    template_name = 'blogs/blog.html'


class PostView(DetailView):

    queryset = Post.objects.all()
    template_name = 'blogs/post.html'


class CreatePost(CreateView):

    template_name = 'blogs/add_post.html'
    model = Post
    fields = ('title', 'text', 'blog')
    success_url = '/blogs/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class CreatePostInBlog(CreateView):

    template_name = 'blogs/add_post_in_blog.html'
    model = Post
    fields = ('title', 'text')
    success_url = '/blogs/'
    blog = None

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=kwargs['pk'])
        self.success_url += kwargs['pk']
        return super(CreatePostInBlog, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreatePostInBlog, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.blog
        return super(CreatePostInBlog, self).form_valid(form)


class UpdatePost(UpdateView):

    template_name = 'blogs/edit_post.html'
    model = Post
    fields = ('title', 'text')
    success_url = '/blogs/post/'

    def dispatch(self, request, *args, **kwargs):
        self.success_url += kwargs['pk']
        return super(UpdatePost, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


class CreateCategory(CreateView):

    template_name = 'blogs/add_category.html'
    model = Category
    fields = ('name',)
    success_url = '/blogs/'

    def form_valid(self, form):
        return super(CreateCategory, self).form_valid(form)


class CategoryView(DetailView):

    queryset = Category.objects.all()
    template_name = 'blogs/category.html'
