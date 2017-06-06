# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DescribeModel(models.Model):
    name = models.CharField(max_length=100)
    headline = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(DescribeModel):
    Author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True) #TODO: remove null=true and add a default author id:0 gh:1
    picture = models.ImageField()
    analytic = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Author(DescribeModel):

    def __str__(self):
        return self.name

class Comment(models.Model):
    Post = models.ForeignKey('Post', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.Post
