import yfinance as yf
import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
import bs4 as bs
import requests


def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'}
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies', headers=headers)
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    #     with open("sp500tickers.pickle","wb") as f:
    #         pickle.dump(tickers,f)
    return tickers
