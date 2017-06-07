# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def list(request):
    return render(request, 'blog/list.html', {"posts": Post.objects.all(), 'recent': Post.objects.order_by('-id')[:3]})

def details(request, id):
    return render(request, 'blog/details.html', {"post": get_object_or_404(Post,pk=id)})
