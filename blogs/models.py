from __future__ import unicode_literals
from django.conf import settings
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name


class Blog(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ManyToManyField(Category)


class Post(models.Model):

    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)


class Like(models.Model):

    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    data = models.DateTimeField()
    count = models.IntegerField()
