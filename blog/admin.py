# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "1 item was"
    else:
        message_bit = "%s items were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
make_published.short_description = "Mark selected as published"

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["name","Author","created_at","updated_at","status"]
    list_filter = ["updated_at","created_at"]
    search_fields = ["name","headline","analytic"]
    ordering = ['name']
    actions = [make_published]
    class Meta:
        model = models.Post

class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["name","created_at","status"]
    search_fields = ["name","headline"]
    ordering = ['name']
    actions = [make_published]
    class Meta:
        model = models.Author

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["Post","User"]
    class Meta:
        model = models.Comment


admin.site.register(models.Post, PostModelAdmin)
admin.site.register(models.Author, AuthorModelAdmin)
admin.site.register(models.Comment)
