import pandas as pd
import FinanceDataReader as fdr
import pandas_datareader as pdr
import numpy as np
import time
from datetime import datetime
from .models import Test

myStock = ['삼성전자', '삼성전자우', 'SK하이닉스', 'TIGER TOP10', 'TIGER 차이나전기차SOLACTIVE', 'TIGER 2차전지테마', 'KODEX 2차전지산업', '강원랜드','대한항공']
myStockUS = ['SPY', 'AAPL', 'QQQ', 'MSFT', 'GOOGL', 'SPYD', 'ARKK', 'KO', 'RSP', 'IIVI', 'TSLA', 'AMZN', 'O', 'ARKG','VZ', 'JPM', 'PRNT', 'VGAC']
myStockUS = myStockUS + ['SCHB', 'TLT', 'EWU', 'VWO', 'EWG', 'VWOB', 'VTIP', 'EWH', 'EWJ', 'VTEB', 'LQD', 'EWA']
myStockList = []
myCodeList = []
data = []
seriesForConcat = []
startdate = datetime(2020, 1, 1)
enddate = datetime.today()


def findMyDailyStockPrice2():
    krx = pd.read_csv('krx.csv', encoding="cp949")
    start = time.time()
    for m in myStock:
        name = krx.loc[krx['Name'] == m, ['Name', 'Symbol']]['Name'].tolist()[0]
        # print(name)
        code = str(krx.loc[krx['Name'] == m, ['Name', 'Symbol']]['Symbol'].tolist()[0])
        # print(code)
        myStockList.append(name)
        myCodeList.append(code)
    # print(myStockList)
    # print(myCodeList)

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

    # Concat 할 개별 주식의 일별 시세 시리즈형 자료를 출력하여 빈 리스트(emt)에 채워넣는 작업
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
    print('처리시간 : ' + str(finish) + '초')

    return dfMyStock.to_csv('test01.csv')

def mytest():
    Test.objects.create(name='test')