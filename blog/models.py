# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.

# Abstract class

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class DescribeModel(TimestampModel):
    name = models.CharField(max_length=100)
    headline = models.TextField()
    status = models.CharField(max_length=1, choices=(
        ('d', 'Draft'),
        ('p', 'Published'),
    ))
    class Meta:
        abstract = True

# Models

class Post(DescribeModel):
    Author = models.ForeignKey('Author', on_delete=models.CASCADE, default=1)
    picture = models.ImageField()
    analytic = models.TextField(blank=True)
    User = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Author(DescribeModel):

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Comment(TimestampModel):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    Post = models.ForeignKey('Post', on_delete=models.CASCADE)
    body = models.TextField()

    def __unicode__(self):
        return self.Post.name + " - " + self.User.username

    def __str__(self):
        return self.Post.name + " - " + self.User.username
