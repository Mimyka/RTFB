# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    resume = models.TextField()
    text = models.TextField()
    picture = models.ImageField(upload_to="upl")

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50)
    resume = models.TextField()

    def __str__(self):
        return self.name
