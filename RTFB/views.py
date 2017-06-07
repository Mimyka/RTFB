# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post

# Create your views here.

def index(request):
    return render(request, 'pages/index.html', {
    'posts': Post.objects.filter(status__exact='p'),
    'recent': Post.objects.filter(status__exact='p').order_by('-id')[:4],
    })

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def login(request):
    return render(request, 'pages/login.html')
