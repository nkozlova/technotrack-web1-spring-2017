from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from .models import Comment
from blogs.models import Post


class CreateComment(CreateView):

    template_name = 'comments/add_comment.html'
    model = Comment
    fields = ('text',)
    postid = None
    pk = None

    def dispatch(self, request, *args, **kwargs):
        self.postid = get_object_or_404(Post, id=kwargs['pk'])
        self.pk = kwargs['pk']
        return super(CreateComment, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("blogs:post", args=(self.pk, ))

    def get_context_data(self, **kwargs):
        context = super(CreateComment, self).get_context_data(**kwargs)
        context['post'] = self.postid
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.postid
        return super(CreateComment, self).form_valid(form)