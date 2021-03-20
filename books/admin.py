from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'slug']
    list_editable = ['category', 'slug']
    #list_filter = []
    #search_fields = []
    #ordering = ['-client', 'line', 'order']

admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'slug']
    list_editable = ['category', 'slug']

admin.site.register(Subcategory, SubcategoryAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_editable = ['name', 'slug']

admin.site.register(Book, BookAdmin)

class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ['id', 'title_text', 'sub_title', 'title_photo', 'written_by', 'slug', 'created']
    list_editable = ['title_text', 'sub_title', 'title_photo', 'slug']
    ordering = ['-created']

admin.site.register(Article, ArticleAdmin)