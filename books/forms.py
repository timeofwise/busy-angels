from django import forms
from .models import Article
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