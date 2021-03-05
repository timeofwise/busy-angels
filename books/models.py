from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(max_length=20, null=True)
    # slug
    slug = models.SlugField(max_length=50, db_index=True, unique=True, allow_unicode=True, null=True)

    def __str__(self):
        return self.category

class Subcategory(models.Model):
    category = models.CharField(max_length=30, null=True)
    main_category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    # slug
    slug = models.SlugField(max_length=50, db_index=True, unique=True, allow_unicode=True, null=True)

    def __str__(self):
        return self.category

class Book(models.Model):
    name = models.CharField(max_length=40, null=True)
    author = models.CharField(max_length=25, null=True)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.PROTECT, null=True)

    # slug
    slug = models.SlugField(max_length=50, db_index=True, unique=True, allow_unicode=True, null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title_text = models.CharField(max_length=50, null=True)
    title_photo = models.ImageField(upload_to='img/blog_article', default='img/blog/no_image.png', null=True)
    sub_title = models.CharField(max_length=100, null=True)
    written_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True)
    body = models.TextField(null=True)


    # slug
    slug = models.SlugField(max_length=50, db_index=True, unique=True, allow_unicode=True, null=True)

    # datetime create
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title_text