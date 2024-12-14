'''
Using yfinance to get minute historical data
    The period must be within the last 30 days
    Only seven days of 1m granularity are allowed per request

'''
import yfinance as yf

#Create a Ticker object

goog = yf.Ticker('goog')
#aapl = yf.Ticker('aapl')
#msft = yf.Ticker('msft')

#Fetch the data

data = goog.history(interval='1m', start='2024-12-01', end='2024-12-08')

print(data)