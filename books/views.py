from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy
import fnmatch, os, random
from datetime import datetime, timedelta, date

#number_files = len(fnmatch.filter(os.listdir('static/img/'), '*.jpg'))
number_files = len(fnmatch.filter(os.listdir('/home/busyangels/busy-angels/static/img/'), '*.jpg'))

def books(request):
    today = datetime.today()
    articles = Article.objects.all()
    rand = random.randint(1, number_files)

    return render(request, 'books/blog.html', {
        'articles':articles,
        'rand': rand,
        'today':today,
    })

def AddBook(request):

    if request.method == "POST":
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.save()
            #return render(request, 'books/blog.html', {'form': article, 'rand':rand})
            return redirect('books')
    else:
        book_form = BookForm()
    return render(request, 'books/book_add_book.html', {'form':book_form})


def post(request):
    rand = random.randint(1, number_files)

    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.save()
            #return render(request, 'books/blog.html', {'form': article, 'rand':rand})
            return redirect('books')
    else:
        article_form = ArticleForm()
    return render(request, 'books/post.html', {'form':article_form,'rand':rand})


def blogSingle(request, article_slug):
    rand = random.randint(1, number_files)

    template = 'books/blog-single.html'
    article = Article.objects.filter(slug=article_slug)
    context = {
        'rand':rand,
        'article':article,
    }
    return render(request, template, context)