from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('upload-csv/', upload_csv, name="upload_csv"),
    path('read-csv/', ReadCSV, name="read"),
]