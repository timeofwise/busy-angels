from django.urls import path
from .views import *

urlpatterns = [
    path('', assets_scroll, name='assets'),
    path('data-refresh/', GetDataRefesh, name='data_refresh'),
    path('add-cash/', AddCashFlow.as_view(), name='add_cash'),
    path('add-exchange/', AddExchange, name='add_exchange'),
    path('add-stock/', AddStockTrade, name='add_stock'),
    path('insert-stock-data/', InsertStockTradeData, name='insert_stock_data'),
    path('test/', entry_index, name='test'),
]