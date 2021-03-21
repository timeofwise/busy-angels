from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='books'),
    path('article/<str:article_slug>/', blogSingle, name='blog-single'),
    path('add-book/', AddBook, name='add-book'),
    path('add-scrap/', AddScrap, name='add-scrap'),
    path('add-post/', post, name='add-post'),
]