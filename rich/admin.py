from django.contrib import admin
from .models import *

# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'date']
    #list_editable = ['category', 'slug']
    list_filter = ['date']
    #search_fields = []
    ordering = ['-date']

admin.site.register(Asset, AssetAdmin)