# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["name","Author","created_at","updated_at"]
    list_filter = ["updated_at","created_at"]
    search_fields = ["name","headline","analytic"]
    class Meta:
        model = models.Post

class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["name","created_at"]
    search_fields = ["name","headline"]
    class Meta:
        model = models.Author

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["Post","User"]
    class Meta:
        model = models.Comment

admin.site.register(models.Post, PostModelAdmin)
admin.site.register(models.Author, AuthorModelAdmin)
admin.site.register(models.Comment)
