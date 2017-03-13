from django.views.generic.base import TemplateView

from blogs.models import Blog, Post
from comments.models import Comment


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blogs_count'] = Blog.objects.all().count()
        context['posts_count'] = Post.objects.all().count()
        context['comments_count'] = Comment.objects.all().count()
        return context