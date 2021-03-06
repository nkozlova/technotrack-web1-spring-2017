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

    def __unicode__(self):
        return self.title


class Post(models.Model):

    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.title


class Like(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)

