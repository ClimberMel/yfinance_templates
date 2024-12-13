
import pandas as pd
import yfinance as yf
#from yahoofinancials import YahooFinancials

aapl_df = yf.download('AAPL')

df = pd.DataFrame(aapl_df)
#df.to_csv('AAPL.csv')
print(df)