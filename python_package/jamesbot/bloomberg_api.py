import pandas as pd
from datetime import datetime, timedelta
from xbbg import blp

# Call Bloomberg API
def get_data(ticker, start_date, end_date):
    
    print('Getting data from Bloomberg for',ticker,'...')
    df = blp.bdh(tickers=ticker, flds=['Open', 'High', 'Low', 'Last_Price', 'Volume'], \
        start_date=to_str(start_date - timedelta(days=1)),\
        end_date=to_str(end_date + timedelta(days=1)),)
    # Delete Multi-level index
    df.columns = df.columns.droplevel(0)

    return df

def to_str(dt_date):
    return dt_date.strftime('%Y-%m-%d')