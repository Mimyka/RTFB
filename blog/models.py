# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

    #
   # #   #####   ####  ##### #####    ##    ####  #####
  #   #  #    # #        #   #    #  #  #  #    #   #
 #     # #####   ####    #   #    # #    # #        #
 ####### #    #      #   #   #####  ###### #        #
 #     # #    # #    #   #   #   #  #    # #    #   #
 #     # #####   ####    #   #    # #    #  ####    #


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class DescribeModel(TimestampModel):
    name = models.CharField(max_length=100)
    headline = models.TextField()
    class Meta:
        abstract = True

class DraftModel(models.Model):
    status = models.CharField(max_length=1, choices=(
        ('d', 'Draft'),
        ('p', 'Published'),
    ))
    class Meta:
        abstract = True

class UserModel(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    class Meta:
        abstract = True


 #     # ####### ######  ####### #        #####
 ##   ## #     # #     # #       #       #     #
 # # # # #     # #     # #       #       #
 #  #  # #     # #     # #####   #        #####
 #     # #     # #     # #       #             #
 #     # #     # #     # #       #       #     #
 #     # ####### ######  ####### #######  #####

# ===========================
#            Post
# ===========================

# Post.created_at
# Post.updated_at
# Post.name
# Post.headline
# Post.status
# Post.Author -> [name,headline,User]
# Post.picture -> [url,...]
# Post.date
# Post.User

class Post(DescribeModel, DraftModel, UserModel):
    Author = models.ForeignKey('Author', on_delete=models.CASCADE, default=1)
    picture = models.ImageField()
    date = models.DecimalField(decimal_places=0,max_digits=4, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

# ===========================
#          Analytic
# ===========================

# Analytic.created_at
# Analytic.updated_at
# Analytic.status
# Analytic.part
# Analytic.content
# Analytic.extract
# Analytic.User
# Analytic.Post -> [name, picture...]

class Analytic(TimestampModel, DraftModel, UserModel):
    Post = models.ForeignKey('Post')
    part = models.CharField(max_length=255)
    content = models.TextField()
    extract = models.TextField()

    def __unicode__(self):
        return self.Post.name + " - " + self.part

    def __str__(self):
        return self.Post.name + " - " + self.part


# ===========================
#           AUTHOR
# ===========================

# Author.name
# Author.headline
# Author.User
# Author.picture

class Author(DescribeModel, UserModel):
    picture = models.ImageField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

# ===========================
#          COMMENT
# ===========================

# Comment.created_at
# Comment.updated_at
# Comment.User
# Comment.Post
# Comment.body

class Comment(TimestampModel, UserModel):
    Post = models.ForeignKey('Post')
    body = models.TextField()

    def __unicode__(self):
        return self.Post.name + " - " + self.User.username

    def __str__(self):
        return self.Post.name + " - " + self.User.username
