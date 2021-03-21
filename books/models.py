from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
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
    cover = models.ImageField(upload_to='img/books/cover-img', default='img/books/cover-img/no_image.png', null=True)
    author = models.CharField(max_length=25, null=True)
    translated = models.BooleanField(default=False, null=True)
    translator = models.CharField(max_length=15, null=True)
    publisher = models.CharField(max_length=15, null=True)
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

    def get_absolute_url_articles(self):
        #상세페이지 출력
        return reverse('blog-single', args=[self.slug])

    @property
    def time_diff(self):
        today = datetime.today()
        diff = (today - self.created).total_seconds()
        out = ''
        if diff < 60:
            out = out + str(round(diff)) + '초 전'
        elif diff < 3600:
            out = out + str(round(diff / 60)) + '분 전'
        elif diff < 86400:
            out = out + str(round(diff / 3600)) + '시간 전'
        elif diff < 2592000:
            out = out + str(round(diff / 86400)) + '일 전'
        elif diff < 31104000:
            out = out + str(round(diff / 2592000)) + '개월 전'
        else:
            out = out + str(round(diff / 31104000)) + '년 전'

        return out

    def __str__(self):
        return self.title_text

class Scrap(models.Model):
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name="scrap", null=True)
    quote = models.TextField(null=True)
    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)