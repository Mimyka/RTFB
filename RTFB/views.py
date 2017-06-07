# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post

# Create your views here.

def index(request):
    return render(request, 'pages/index.html', {
    'posts': Post.objects.all(),
    'recent': Post.objects.order_by('-id')[:3],
    })

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
