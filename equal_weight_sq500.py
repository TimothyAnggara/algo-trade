
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secret import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('sp_500_stocks.csv')
print(stocks)

symbol = 'aapl'
api_url = f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}"
data = requests.get(api_url).json()
print(data)

price = data['latestPrice']
market_cap = data['marketCap']

print(price, market_cap)

my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)

final_dataframe = final_dataframe.append(
                    pd.Series(['AAPL', 
                            data['latestPrice'], 
                            data['marketCap'], 
                            'N/A'], 
                            index = my_columns), 
                            ignore_index = True)

final_dataframe = pd.DataFrame(columns = my_columns)
for stock in stocks['Ticker'][:5]:
    api_url = f"https://cloud.iexapis.com/stable/stock/{stock}/quote?token={IEX_CLOUD_API_TOKEN}"
    data = requests.get(api_url).json()
    
    final_dataframe = final_dataframe.append(
        pd.Series(
            [
                stock,
                data['latestPrice'],
                data['marketCap'],
                'N/A'
            ], index = my_columns)
    , ignore_index = True)

print(final_dataframe)