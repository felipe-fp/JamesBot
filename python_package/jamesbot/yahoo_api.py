import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf

# Call Yahoo Finance API
def get_data(ticker, start_date, end_date):
    print('Getting data from Yahoo for',ticker,'...')
    return yf.Ticker(ticker).history(start = to_str(start_date + timedelta(days=1)), end = to_str(end_date + timedelta(days=1)))

def to_str(dt_date):
    return dt_date.strftime('%Y-%m-%d')