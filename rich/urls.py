from django.urls import path
from .views import *

urlpatterns = [
    path('', assets, name='assets'),
]