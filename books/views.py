from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from django.urls import reverse_lazy
import fnmatch, os, random

def books(request):
    articles = Article.objects.all()

    return render(request, 'books/blog.html', {
        'articles':articles,
    })

def post(request):
    articles = Article.objects.all()


    #jpg_list = os.listdir('static/img/')  # dir is your directory path
    number_files = len(fnmatch.filter(os.listdir('static/img/'), '*.jpg'))
    rand = random.randint(1,number_files)

    return render(request, 'books/post.html', {
        'articles':articles,
        'rand':rand,
    })