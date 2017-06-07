# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Q

# Create your views here.

def list(request):
    queryset_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
        Q(name__icontains=query) |
        Q(Author__name__icontains=query)
        )
    return render(request, 'blog/list.html', {
    'posts': queryset_list,
    })

def details(request, id):
    return render(request, 'blog/details.html', {
    'post': get_object_or_404(Post,pk=id),
    })
