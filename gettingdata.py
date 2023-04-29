import pandas as pd
import matplotlib.pyplot as plt
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
#функция для обработки цены
def clean(data):
    for i in range(len(data)):

        if '.' in data[i]:
            data[i]=(data[i][0:data[i].index('.')])

        data[i]=data[i].replace(',', '.')
    return data.astype(float)
#функция для обработки изменения в процентах
def cleanchange(data):
    for i in range(len(data)):
        if '%' in data[i]:
            data[i] = data[i][0:data[i].index('%')]

    return data.astype(float)
def go():
    #считываем
    btc_data=pd.read_csv('Bitcoin Historical Data - Investing.com.csv')
    eth_data=pd.read_csv('Ethereum Historical Data - Investing.com.csv')
    btc_data=btc_data[['Date','Price','Change %']]
    eth_data=eth_data[['Date','Price','Change %']]
    #очищаем
    btc_data['Price']=clean(btc_data['Price'])
    eth_data['Price']=clean(eth_data['Price'])
    btc_data['Change %']=cleanchange(btc_data['Change %'])
    eth_data['Change %']=cleanchange(eth_data['Change %'])
    #рисуем графики для анализа
    fig, ax = plt.subplots(figsize=(12, 12), nrows=2, ncols=2)
    fig.suptitle('analytical charts')
    ax[0,0].plot([i for i in range(0,200)], btc_data['Price'][0:200], label='BTC')
    ax[0,0].set_title('BTCUSDT')
    ax[0,0].set_xlabel('days before this day')
    ax[0,0].set_ylabel('Price')
    ax[0,1].plot([i for i in range(0,200)], eth_data['Price'][0:200], label='ETH')
    ax[0,1].set_title('ETHUSDT')
    ax[0,1].set_xlabel('days before this day')
    ax[0,1].set_ylabel('Price')
    ax[1,0].plot(btc_data['Change %'][0:50],label='BTCUSDT')
    ax[1,0].plot(eth_data['Change %'][0:50],label='ETHUSDT',linestyle='dashed')
    ax[1,0].set_title('% to %')
    ax[1,0].legend()
    ax[1,1].plot([i for i in range(0,50)], btc_data['Price'][0:50], label='BTC')
    ax[1, 1].plot([i for i in range(0,50)], eth_data['Price'][0:50], label='ETH',linestyle='dashed')
    ax[1, 1].set_title('BTCUSDT and ETHUSDT')
    ax[1, 1].legend()
    plt.show()
    return btc_data,eth_data
