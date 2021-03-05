from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from django.urls import reverse_lazy


def books(request):
    articles = Article.objects.all()

    return render(request, 'books/blog.html', {
        'articles':articles,
    })