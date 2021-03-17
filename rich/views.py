from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from el_pagination.decorators import page_template
from django.urls import reverse_lazy
from datetime import datetime, timedelta
import time
from django.db.models import Avg, Max, Min, Sum, Count
from .forms import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

import pandas as pd
import FinanceDataReader as fdr
import pandas_datareader as pdr





def assets_scroll(request):
    template = 'rich/blog.html'
    count = Asset.objects.all()
    assets_all = Asset.objects.all().order_by('-date')


    kl_list = range(1,100)
    startpoint = '2021-01-01'
    today = datetime.today().strftime("%Y-%m-%d")
    nextday = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    deposits = Cashflow.objects.filter(date__range=[startpoint, today])
    cash_krw = Cashflow.objects.filter(date__range=[startpoint, today]).aggregate(Sum('cash_krw'))['cash_krw__sum']
    cash_usd = Cashflow.objects.filter(date__range=[startpoint, today]).aggregate(Sum('cash_usd'))['cash_usd__sum']


    trade = Stocktrade.objects.filter(date__range=[startpoint, today]).filter(stock_id=1)

    assets_for_list = Asset.objects.all().order_by('date')
    asset_list_in_group = []
    i = 0
    principal_krw = 0
    principal_usd = 0
    stock_krw = 0
    stock_usd = 0

    #stock_assets_krw = Stocktrade.objects.filter(date__range=[startpoint, today]).filter(currency_id=1)

    for asset in assets_for_list:

        # common data
        asset_list = []
        date_for_list = asset.date #str type
        date_for_list_str = date_for_list.strftime("%Y-%m-%d")
        #date_for_list_aware = datetime.strptime(date_for_list, "%Y-%m-%d") #datetimpe type
        index = asset.category.category
        # .aggregate(Sum('cash_krw'))['cash_krw__sum'] --> for recycle

        asset_list.append(date_for_list) #0
        asset_list.append(index) #1
        # ['0:date(당일)', '1:index', '2:원화원금', '3:미화원금', '4:전회대비 원화차액', '5:전회대비 미화차액',
        # '6:한국주식자산','7:미주식자산', '8:리스트번호', '9:계산시작일']

        # queryset for reference when 1st data in asset_list_group
        if i == 0:
            principals = Cashflow.objects.filter(date__range=[startpoint, date_for_list_str])
            stock_assets_krw = Stocktrade.objects.filter(date__range=[startpoint, date_for_list_str]).filter(currency_id=1)
            stock_assets_usd = Stocktrade.objects.filter(date__range=[startpoint, date_for_list_str]).filter(currency_id=2)

            if principals:
                for principal in principals:
                    principal_krw = principal_krw + float(principal.cash_krw * principal.io.constant)
                    principal_usd = principal_usd + float(principal.cash_usd * principal.io.constant)
                asset_list.append(principal_krw) #2
                asset_list.append(principal_usd) #3
                asset_list.append(0) #4
                asset_list.append(0) #5

            else:
                asset_list.append(0) #2
                asset_list.append(0) #3
                asset_list.append(0) #4
                asset_list.append(0) #5

            if stock_assets_krw | stock_assets_usd:
                for stock_asset in stock_assets_krw:
                    stock_krw += stock_asset.price_total
                for stock_asset in stock_assets_usd:
                    stock_usd += stock_asset.price_total
                asset_list.append(stock_krw)  # 6
                asset_list.append(stock_usd)  # 7

            else:
                asset_list.append(0)  # 6
                asset_list.append(0)  # 7

            asset_list.append(i)  # 8
            asset_list.append(startpoint)  # 9



        #((0),(1),(2)...)
        # queryset for reference after 2nd data in asset_list_group
        if i > 0:
            ref_date_of_before_data = (asset_list_in_group[i-1][0] + timedelta(days=1)).strftime("%Y-%m-%d")
            #y=y+ repr(i) +'번째' + ref_date_of_before_data+', '
            #z=z+ repr(i) +'번째' + date_for_list_str+', '
            principals = Cashflow.objects.filter(date__range=[ref_date_of_before_data, date_for_list_str])
            stock_assets_krw = Stocktrade.objects.filter(date__range=[ref_date_of_before_data, date_for_list_str]).filter(currency_id=1)
            stock_assets_usd = Stocktrade.objects.filter(date__range=[ref_date_of_before_data, date_for_list_str]).filter(currency_id=2)

            if principals:
                for principal in principals:
                    principal_krw = principal_krw + float(principal.cash_krw * principal.io.constant)
                    principal_usd = principal_usd + float(principal.cash_usd * principal.io.constant)
                asset_list.append(principal_krw)  #2
                asset_list.append(principal_usd)  #3
                asset_list.append(principal_krw - asset_list_in_group[i-1][2])  #4
                asset_list.append(principal_usd - asset_list_in_group[i-1][3])  #5

            else:
                asset_list.append(asset_list_in_group[i-1][2])  #2
                asset_list.append(asset_list_in_group[i-1][3])  #3
                asset_list.append(0)  #4
                asset_list.append(0)  #5

            if stock_assets_krw | stock_assets_usd:
                for stock_asset in stock_assets_krw:
                    stock_krw += stock_asset.price_total
                for stock_asset in stock_assets_usd:
                    stock_usd += stock_asset.price_total
                asset_list.append(stock_krw)  # 6
                asset_list.append(stock_usd)  # 7

            else:
                asset_list.append(asset_list_in_group[i-1][6])  # 6
                asset_list.append(asset_list_in_group[i-1][7])  # 7
            asset_list.append(i)  # 8
            asset_list.append(ref_date_of_before_data)  # 9



        asset_list_in_group.append(asset_list)
        i += 1

    page = request.GET.get('page', 1)

    j=0
    asset_list_in_group_reverse=[]
    for j in range(len(asset_list_in_group)):
        asset_list_in_group_reverse.append(asset_list_in_group[len(asset_list_in_group)-j-1])

    paginator = Paginator(asset_list_in_group_reverse, 5)
    try:
        assets = paginator.page(page)
    except PageNotAnInteger:
        assets = paginator.page(1)
    except EmptyPage:
        assets = paginator.page(paginator.num_pages)

    return render(request, template, {
        'assets': assets,
        'assets_all':assets_all,
        'count':count,
        'today':today,
        'deposits':deposits,
        'cash_krw':cash_krw,
        'trade':trade,
        'nextday':nextday,
        'asset_list_in_group':asset_list_in_group,
        'x':date_for_list_str,
        'asset_list_in_group_reverse':asset_list_in_group_reverse,
        'stock_assets_krw':stock_assets_krw,
    })




def entry_index(request):
    numbers_list = Asset.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 5)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'test.html', {'numbers': numbers})


class AddCashFlow(CreateView):
    model = Cashflow
    fields = [
        'date',
        'io',
        'cash_krw',
        'cash_usd',
    ]

    success_url = reverse_lazy('assets')
    template_name_suffix = '_add-cash'

def AddExchange(request):
    if request.method == "POST":
        exchange_form = ExchangeForm(request.POST)
        if exchange_form.is_valid():
            new_exchange = exchange_form.save(commit=False)
            new_exchange.save()
            return render(request, 'rich/blog.html', {'new_exchange':new_exchange})
    else:
        exchange_form = ExchangeForm()
    return render(request, 'rich/cashflow_add-exchange.html', {'form':exchange_form})

def AddStockTrade(request):
    template = 'rich/stocktrade_add-stock.html'
    stocks = Stocktrade.objects.all()
    names = Stock.objects.all()
    context = {
        'stocks' : stocks,
        'names' : names,
    }

    return render(request, template, context)


@csrf_exempt
def InsertStockTradeData(request):
    date = request.POST.get('date')
    stock = request.POST.get('stock')
    io = request.POST.get('io')
    currency_trade = request.POST.get('currency_trade')
    price_trade = request.POST.get('price_trade')
    amount = request.POST.get('amount')
    price_std = request.POST.get('price_std')

    try:
        content = Stocktrade(date=date, stock=stock, io=io, currency_trade=currency_trade, price_trade=price_trade, amount=amount, price_std=price_std)
        content.save()
        content_data = {'error': False, 'errorMessage': 'Content added successfully.'}
        return JsonResponse(content_data, safe=False)
    except:
        content_data = {'error': True, 'errorMessage': 'Failed to add Content.'}
        return JsonResponse(content_data, safe=False)

def GetDataRefesh(request):
    template='data/data_refresh.html'

    # PANDAS
    stock_kr = Stock.objects.filter(currency_id=1)
    stock_us = Stock.objects.filter(currency_id=2)
    myStock = []
    myStockUS = []
    for kr in stock_kr:
        myStock.append(kr.name)
    for us in stock_us:
        myStockUS.append(us.name)
    """
    #myStock = ['삼성전자', '삼성전자우', 'SK하이닉스', 'TIGER TOP10', 'TIGER 차이나전기차SOLACTIVE', 'TIGER 2차전지테마', 'KODEX 2차전지산업','강원랜드', '대한항공']
    #myStockUS = ['SPY', 'AAPL', 'QQQ', 'MSFT', 'GOOGL', 'SPYD', 'ARKK', 'KO', 'RSP', 'IIVI', 'TSLA', 'AMZN', 'O','ARKG', 'VZ', 'JPM', 'PRNT', 'VGAC']
    #myStockUS = myStockUS + ['SCHB', 'TLT', 'EWU', 'VWO', 'EWG', 'VWOB', 'VTIP', 'EWH', 'EWJ', 'VTEB', 'LQD', 'EWA']
    """
    myStockList = []
    myCodeList = []
    data = []
    seriesForConcat = []
    startdate = datetime(2020, 1, 1)
    enddate = datetime.today()
    krx = pd.read_csv('rich/krx.csv', encoding="cp949")
    start = time.time()
    for m in myStock:
        name = krx.loc[krx['Name'] == m, ['Name', 'Symbol']]['Name'].tolist()[0]
        # print(name)
        code = str(krx.loc[krx['Name'] == m, ['Name', 'Symbol']]['Symbol'].tolist()[0])
        # print(code)
        myStockList.append(name)
        myCodeList.append(code)
    myDict = dict(zip(myStockList, myCodeList))

    for singleStockName in myStockList:
        empty = []  # 주식명을 가져와서 myDict에서 코드를 색인하는 주식명 리스트를 넘겨주기 위한 임시의 빈리스트 생성
        singleStockCode = myDict[singleStockName]
        singleStockList = fdr.DataReader(singleStockCode)
        empty.append(singleStockName)
        empty.append(singleStockList)
        data.append(empty)
        time.sleep(0.1)

    for singleTickerName in myStockUS:
        empty_us = []
        singleTicker = singleTickerName
        singleTickerList = pdr.get_data_yahoo(singleTicker, startdate, enddate)
        empty_us.append(singleTicker)
        empty_us.append(singleTickerList)
        data.append(empty_us)
        time.sleep(0.1)

    for i in range(len(data)):
        stockName = data[i][0]
        stockSeries = data[i][1]['Close'].rename(stockName)
        seriesForConcat.append(stockSeries)

    dfMyStock = seriesForConcat[0]

    for k in range(len(data) - 1):
        k += 1
        dfMyStock = pd.concat([dfMyStock, seriesForConcat[k]], axis=1)
    finish = time.time() - start
    finish = format(round(finish, 2))
    execute_time = '처리시간 : ' + str(finish) + '초'
    dfMyStock.to_csv('rich/templates/data/data.csv')

    return render(request, template, {
        'df': dfMyStock,
        'ex': execute_time,
    })