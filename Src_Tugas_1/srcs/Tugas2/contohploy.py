import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dts

actual_date =dts.date.today()
last_360_period = actual_date - dts.timedelta(days=360)

BBCA_JK = yf.download('BBCA.JK', start=last_360_period, end=actual_date, interval="1d")

BBCA_JK['ema_9'] = BBCA_JK['Close'].ewm(span=9, adjust=False).mean()
BBCA_JK['ema_21'] = BBCA_JK['Close'].ewm(span=21, adjust=False).mean()
BBCA_JK['ema_55'] = BBCA_JK['Close'].ewm(span=55, adjust=False).mean()
BBCA_JK['ema_100'] = BBCA_JK['Close'].ewm(span=100, adjust=False).mean()
BBCA_JK['ema_200'] = BBCA_JK['Close'].ewm(span=200, adjust=False).mean()

BBCA_JK['Signal'] = 0
BBCA_JK['Signal'] = np.where(BBCA_JK['ema_21']  > BBCA_JK['ema_55'], 1.0,0.0)

BBCA_JK['Position'] = BBCA_JK['Signal'].diff()

BBCA_JK.head()

plt.figure(figsize= (20,10))

BBCA_JK['Close'].plot(color= 'k', label='Close Price')
BBCA_JK['ema_21'].plot(color= 'b', label = '21-EMA')
BBCA_JK['ema_55'].plot(color = 'g', label= '55-EMA')

plt.plot(BBCA_JK[BBCA_JK['Position'] == 1].index,
         BBCA_JK['ema_21'][BBCA_JK['Position'] == 1],
          '^', markersize=15, color='g', label='buy-short-term-bull')

plt.plot(BBCA_JK[BBCA_JK['Position'] == -1].index,
         BBCA_JK['ema_21'][BBCA_JK['Position'] == -1],
          'v', markersize=15, color='r', label='sell-short-term-bear')

plt.ylabel('Price in TL', fontsize=15)
plt.xlabel('Date', fontsize=15)
plt.title('CIMSA', fontsize=20)
plt.legend()
plt.grid()
plt.show() 
BBCA_JK.head()