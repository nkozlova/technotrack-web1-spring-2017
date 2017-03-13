from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from blogs.models import Post


class Comment(models.Model):

    post = models.ForeignKey(Post)
    text = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
