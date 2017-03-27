from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from blogs.models import Blog, Post
from comments.models import Comment
from .models import User
from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blogs_count'] = Blog.objects.all().count()
        context['posts_count'] = Post.objects.all().count()
        context['comments_count'] = Comment.objects.all().count()
        return context


class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    success_url = '/login/'
    template_name = 'core/register.html'

    def form_valid(self, form):
        form.save(commit=True)
        return super(CreateUser, self).form_valid(form)


def register(request):
    if request.method == 'GET':
        form = CreateUser()
    else:
        form = CreateUser(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect('/login/')
    return render(request, 'core/register.html', {'form': form})