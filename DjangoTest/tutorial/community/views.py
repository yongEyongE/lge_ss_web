# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from community.forms import *

# Create your views here.

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    return render(request, 'write.html', {'form':form})

def list(request):
    articleList = Article.objects.all() #모든 컬럼 가져옴
    return render(request, 'list.html', {'articleList': articleList})

#view 로 Article 이라는 객체 전달
def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article': article})