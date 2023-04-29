import json
import requests
import datetime
import pandas as pd
import time

def go(model):
    btc = pd.DataFrame()

    eth = pd.DataFrame()
    currenttime = time.perf_counter()
    while True:

        key1 = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        key2= "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

        data = requests.get(key1)
        data = data.json()
        realtime=time.perf_counter()-currenttime
        btc[realtime]=[data['price']]


        data = requests.get(key2)
        data = data.json()
        eth[realtime]=[data['price']]

        #если имеем две записи и больше то можем оценить колебание
        if len(eth.columns)>1:
            difbtc=(100*(float(btc[btc.columns[len(btc.columns)-1]])-float(btc[btc.columns[len(btc.columns)-2]]) )/float(btc[btc.columns[len(btc.columns)-2]]))
            difeth=(100*(float(eth[eth.columns[len(eth.columns)-1]])-float(eth[eth.columns[len(eth.columns)-2]]) )/float(eth[eth.columns[len(eth.columns)-2]]))
            print("\033[34m {}" .format(f'колебание полное {difeth}%'))
            print("\033[32m {}" .format(f'колебание собственное {difeth-float(model.predict([[difbtc]]))}%'))

        #если уже прошел час то смотрим все за последние 60 мин
        if time.perf_counter()-currenttime>3600:
            last=eth.columns[len(eth.columns)-1]
            pred=time.localtime()
            for i in reversed(eth.columns):
                if float(last)-float(i)>=3600:
                    pred=i
                    break
            change=100*((float(eth[last])-float(eth[pred]))/float(eth[pred]))
            if (change>=1):
                print("\033[33m {}" .format('\n--------------'))
                print("\033[33m {}" .format(f'изменение цены на {change}% '))
                print("\033[33m {}" .format('--------------\n'))




