from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']

admin.site.register(Category, CategoryAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'nation']

admin.site.register(Currency, CurrencyAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'nick']

admin.site.register(Account, AccountAdmin)


class CashflowcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'constant']
    list_editable = ['name', 'constant']

admin.site.register(Cashflowcategory, CashflowcategoryAdmin)

class StocktradecategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'constant']
    list_editable = ['name', 'constant']

admin.site.register(Stocktradecategory, StocktradecategoryAdmin)


class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'currency', 'updated']

admin.site.register(Stock, StockAdmin)

class AssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'date']
    #list_editable = ['category', 'slug']
    list_filter = ['date']
    #search_fields = []
    ordering = ['-date']

admin.site.register(Asset, AssetAdmin)

class CashflowAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'io', 'cash_krw', 'cash_usd']

admin.site.register(Cashflow, CashflowAdmin)

class StocktradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'account', 'io', 'stock', 'unit_price', 'amount', 'price_total']
    list_editable = ['unit_price', 'amount']

admin.site.register(Stocktrade, StocktradeAdmin)