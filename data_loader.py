import yfinace 
import pandas as pd
from datetime import datetime, timedelta

class DataLoarder():
    
    def get_data(self, period, tickers_list):
        data_open = pd.DataFrame(yfinance.Ticker(tickers_list[0]).history(period = period).Open)
        data_open.columns = [tickers_list[0]]

        data_high = pd.DataFrame(yfinance.Ticker(tickers_list[0]).history(period = period).High)
        data_high.columns = [tickers_list[0]]
    
        data_low = pd.DataFrame(yfinance.Ticker(tickers_list[0]).history(period = period).Low)
        data_low.columns = [tickers_list[0]]
        
        data_close = pd.DataFrame(yfinance.Ticker(tickers_list[0]).history(period = period).Close)
        data_close.columns = [tickers_list[0]]

        data_volume = pd.DataFrame(yfinance.Ticker(tickers_list[0]).history(period = period).Volume)
        data_volume.columns = [tickers_list[0]]

        for ticker in tickers_list[1:]:

            ticker_open = pd.DataFrame(yfinance.Ticker(ticker).history(period = period).Open)
            ticker_open.columns = [ticker]

            ticker_high = pd.DataFrame(yfinance.Ticker(ticker).history(period = period).High)
            ticker_high.columns = [ticker]

            ticker_low = pd.DataFrame(yfinance.Ticker(ticker).history(period = period).Low)
            ticker_low.columns = [ticker]

            ticker_close = pd.DataFrame(yfinance.Ticker(ticker).history(period = period).Close)
            ticker_close.columns = [ticker]

            ticker_volume = pd.DataFrame(yfinance.Ticker(ticker).history(period = period).Volume)
            ticker_volume.columns = [ticker]
            
            if len(ticker_close.index) != 0:
                data_open = data_open.join(ticker_open, how = 'outer')
                data_high = data_high.join(ticker_high, how = 'outer')
                data_low = data_low.join(ticker_low, how = 'outer') 
                data_close = data_close.join(ticker_close, how = 'outer')
                data_volume = data_volume.join(ticker_volume, how = 'outer')
            else:
                print('Ticker not Available')

        self.open_prices = data_open
        self.high_prices = data_high
        self.low_prices = data_low
        self.close_prices = data_close
        self.volume = data_volume
