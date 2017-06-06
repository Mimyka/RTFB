# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="upl")
    headline = models.TextField()
    analytic = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    resume = models.TextField()

    def __str__(self):
        return self.name
