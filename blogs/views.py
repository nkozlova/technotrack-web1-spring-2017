# coding: utf-8
from django.shortcuts import get_object_or_404, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from .models import Blog, Post, Category, Like
from django import forms
from django.http import JsonResponse


class SortForm(forms.Form):

    sort = forms.ChoiceField(choices=(
        ('title', u'Заголовок'),
        ('description', u'Описание'),
    ),
        required=False, widget=forms.RadioSelect,
    )
    search = forms.CharField(required=False, widget=forms.TextInput)


class UpdateBlog(UpdateView):

    template_name = 'blogs/edit_blog.html'
    model = Blog
    fields = ('title', 'description', 'category')

    def dispatch(self, request, *args, **kwargs):
        return super(UpdateBlog, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("blogs:blog", args=(self.object.pk, ))

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)


class CreateBlog(CreateView):

    template_name = 'blogs/add_blog.html'
    model = Blog
    fields = ('title', 'description', 'category')

    def get_success_url(self):
        return reverse("blogs:blog", args=(Blog.objects.all().count(),))

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
            val = self.sortform.cleaned_data.get('sort')
            if val:
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


class PostCommentsView(DetailView):

    queryset = Post.objects.all()
    template_name = 'blogs/commentsdiv.html'


class CreatePost(CreateView):

    template_name = 'blogs/add_post.html'
    model = Post
    fields = ('title', 'text', 'blog')

    def get_form(self, form_class=None):
        form = super(CreatePost, self).get_form(form_class=form_class)
        form.fields['blog'].queryset = self.request.user.blog_set.all()
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)

    def get_success_url(self):
        return reverse("blogs:post", args=(Post.objects.all().count(),))


class CreatePostInBlog(CreateView):

    template_name = 'blogs/add_post_in_blog.html'
    model = Post
    fields = ('title', 'text')
    blog = None

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, id=kwargs['pk'])
        return super(CreatePostInBlog, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreatePostInBlog, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = self.blog
        return super(CreatePostInBlog, self).form_valid(form)

    def get_success_url(self):
        return reverse("blogs:post", args=(Post.objects.all().count(), ))


class UpdatePost(UpdateView):

    template_name = 'blogs/edit_post.html'
    model = Post
    fields = ('title', 'text')

    def get_success_url(self):
        return reverse("blogs:post", args=(self.object.pk, ))

    def dispatch(self, request, *args, **kwargs):
        return super(UpdatePost, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


class CreateCategory(CreateView):

    template_name = 'blogs/add_category.html'
    model = Category
    fields = ('name',)

    def get_success_url(self):
        return reverse("blogs:blog_list")

    def form_valid(self, form):
        return super(CreateCategory, self).form_valid(form)


class CategoryView(DetailView):

    queryset = Category.objects.all()
    template_name = 'blogs/category.html'


class PostLikeCountView(View):

    post = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post = get_object_or_404(Post, pk=pk)
        return super(PostLikeCountView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse(Like.objects.filter(post=self.post).count())


def likes_add(request, pk=None):
    post = get_object_or_404(Post, id=pk)
    if request.user.is_authenticated():
        like = Like.objects.filter(post=post, author=request.user).first()
        if not like:
            like = Like.objects.create(post=post, author=request.user)
        else:
            like.delete()

    return HttpResponse(Like.objects.filter(post=post).count())
