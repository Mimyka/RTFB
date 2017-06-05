# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def list(request):
    return render(request, 'blog/list.html')

def details(request, id):
    return render(request, 'blog/details.html', locals())
