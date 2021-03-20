from django.urls import path
from .views import *

urlpatterns = [
    path('', storage, name='my_storage'),
    path('add/',StorageAddView.as_view(), name='add_storage')
]