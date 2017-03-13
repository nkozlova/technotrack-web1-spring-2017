from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Comment


class CommentView(DetailView):

    queryset = Comment.objects.all()
    template_name = 'comments/comment.html'
