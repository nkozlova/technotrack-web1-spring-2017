from __future__ import unicode_literals
from django.conf import settings
from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)


class Post(models.Model):

    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

