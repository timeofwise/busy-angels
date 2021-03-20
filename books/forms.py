from django import forms
from .models import Article, Book
from django_summernote.widgets import SummernoteWidget

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title_text',
            'title_photo',
            'sub_title',
            'written_by',
            'book',
            'body',
            'slug',
        ]
        widgets = {
            'body': SummernoteWidget(),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'cover',
            'author',
            'translated',
            'translator',
            'publisher',
            'sub_category',
            'slug',
        ]
