
import pandas as pd
import yfinance as yf
#from yahoofinancials import YahooFinancials

aapl_df = yf.download('AAPL')

df = pd.DataFrame(aapl_df)

#If you uncomment the line below it wil write the data to a csv file in the current folder
#df.to_csv('AAPL.csv')
print(df)