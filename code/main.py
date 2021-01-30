import yfinance as yf
import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
import bs4 as bs
import requests

import utility as util

# 1. getting S&P 500 companies ticker list
# 2. use yfinance api module to download all historical data
# def get_all_historical_data():

#
# for stock in stocks:
#     stock = stock.strip()
#     if stock not in ['BRK.B', 'BF.B']:
#         stock_data = yf.Ticker(stock)
#         df = stock_data.history(period='1y')
#         df['TICKER'] = stock
#
#         # creating MA indicator
#         df['20MA'] = df['Close'].rolling(20).mean()
#         df['60MA'] = df['Close'].rolling(60).mean()
#         df['120MA'] = df['Close'].rolling(120).mean()
#
#         condition1 = (df['Volume'] > 1000000)
#
#         condition2 = (df['Close'] > df['20MA'])
#         condition3 = (df['20MA'] > df['20MA'].shift(1))
#         condition4 = (df['60MA'] > df['60MA'].shift(1))
#         #         condition5 = (df['120MA'] < df['120MA'].shift(1))
#
#         condition6 = (df['20MA'] > df['60MA'])
#         condition6 = (df['20MA'] > df['120MA'])
#         condition7 = (df['60MA'] < df['120MA'])
#
#         df.loc[condition1 & condition2 & condition3 & condition4 & condition6 & condition7, 'signal'] = 1
#
#         if df.iloc[-1]['signal'] == 1:
#             df.to_csv('../Data/SP500_REVERSE_TREND/{}.csv'.format(stock))

# hist['Close'].plot(figsize=(20,10))

if __name__ == '__main__':
    stocks = util.save_sp500_tickers()
    df_full = pd.DataFrame()

    print(type(stocks))