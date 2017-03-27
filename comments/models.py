from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from blogs.models import Post


class Comment(models.Model):

    post = models.ForeignKey(Post)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
