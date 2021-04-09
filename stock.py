import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class Stock():

    def __init__(self, ticker):

        self.ticker = ticker 
        try:
            file = open('./data/'+ ticker + '_metadata.txt','r')
            lines = file.readlines()
            self.periods = []
            for line in lines:
                splited = line.split(' ')
                self.periods.append([splited[0],splited[1]])
            file.close()

        except FileNotFoundError:
            print('Creating new Stock metadata for', ticker)
            self.periods = []
            file = open('./data/' + ticker + '_metadata.txt','w')
            file.close()

    def _get_data(self, start_date, end_date):
        
        print('Getting data from Yahoo for',self.ticker,'...')
        ticker_info = yf.Ticker(self.ticker).history(start = start_date, end = end_date)
        print('Saving','...')
        ticker_info.to_csv('./data/' + self.ticker +'_'+ start_date+'_' + end_date + '.csv')
        print('Completed!')

        return ticker_info.loc[start_date:end_date]

    def _load_data(self, start_date, end_date):
        
        if [start_date,end_date] in self.periods:
            try:
                df = pd.read_csv('./data/' + self.ticker +'_'+ start_date+'_' + end_date + '.csv',index_col = 0)
                df.index = pd.to_datetime(df.index)
                return df
            except FileNotFoundError:
                print('[LOAD] File not found (serious problem)', self.ticker)
        else:
            print('[LOAD] File not found (serious problem 2)', self.ticker)


    def fill_voids(self,start_date, end_date):

        dt_start = to_dat(start_date)
        dt_end = to_dat(end_date)

        periods = []

        for period in self.periods:

            period_start = to_dat(period[0])
            period_end = to_dat(period[1])
            
            if period_end >= dt_start and period_start <= dt_end:
                periods.append({'period':period,'concerned':True,'loaded':True})
            else:
                periods.append({'period':period,'concerned':False,'loaded':True})
            
        print('[dict created]',periods)
        first_concerned = None
        flag = True
        last_concerned = None
        n_concerned = 0

        for i in range(len(periods)):
            if periods[i]['concerned']:
                n_concerned += 1
                if flag:
                    flag = False
                    first_concerned = i
                last_concerned = i

        # Correct left void
        if not first_concerned is None:
            if to_dat(periods[first_concerned]['period'][0]) > dt_start: 
                periods[first_concerned:first_concerned] = [{'period':[start_date,to_str(to_dat(periods[first_concerned]['period'][0])-timedelta(days = 1))],'concerned':True,'loaded':False}]
                last_concerned += 1
                n_concerned += 1 

        # Correct right void
        if not last_concerned is None:
            if to_dat(periods[last_concerned]['period'][1]) < dt_end:
                periods[last_concerned+1:last_concerned+1] = [{'period':[to_str(to_dat(periods[last_concerned]['period'][1])+timedelta(days = 1)),end_date],'concerned':True,'loaded':False}]
                n_concerned += 1
        
        # Fill voids
        for i in range(len(periods)-1):
            if periods[i]['concerned'] and periods[i+1]['concerned']:
                period_start = (to_dat(periods[i]['period'][1]) + timedelta(days = 1))
                period_end = (to_dat(periods[i+1]['period'][0]) - timedelta(days = 1))
                
                if period_end > period_start:
                    period = [to_str(period_start),to_str(period_end)]
                    periods[i+1:i+1] = [{'period':period,'concerned':True,'loaded':False}]
        
        if n_concerned == 0:
            # periods.append({'period':[start_date,end_date],'concerned':True,'loaded':False})
            periods = self.add_in_periods(periods, {'period':[start_date,end_date],'concerned':True,'loaded':False})
        return periods

    def load(self, start_date, end_date):

        periods = self.fill_voids(start_date, end_date)
        df = pd.DataFrame()
        print('1',periods)

        n_concerned = 0
        for period in periods:
            if period['concerned']:
                if period['loaded']:
                    df = df.append(self._load_data(period['period'][0], period['period'][1]))
                else:
                    df = df.append(self._get_data(period['period'][0],period['period'][1]))
            n_concerned += 1
        
        if n_concerned > 1:
            df_start = to_str(df.index[0])
            df_end = to_str(df.index[-1])
            df.to_csv('./data/' + self.ticker +'_'+ df_start+'_' + df_end + '.csv')
            periods = self.delete_overlapping(periods,df_start,df_end)
            

        # Translate to official version
        self.periods = []
        print(periods)
        for period in periods:
            self.periods.append([period['period'][0],period['period'][1]])
            
        self.refresh_metadata()
        
        cropped_df = df.loc[start_date : end_date]
        return cropped_df
    
        
    def delete_overlapping(self,periods, df_start, df_end): 
        # It also update periods with the new db
        import os
        periods_ = []
        flag = True
        for period in periods:
            if period['concerned']:
                if flag:
                    periods_.append({'period':[df_start, df_end],'concerned':True,'loaded':True})
                    flag = False
                os.remove('./data/' + self.ticker +'_' +period['period'][0] +  '_' + period['period'][1] + '.csv')
            else:
                periods_.append(period)
        return periods_  

    def refresh_metadata(self): 
        try:
            file = open('./data/' + self.ticker + '_metadata.txt','w')
            for period in self.periods:
                line = period[0]+' '+period[1]+' \n'
                file.write(line)
            file.close()    
        except FileNotFoundError:
            print('MetaData not found for', self.ticker)
            file = open('./data/' + self.ticker + '_metadata.txt','w')
            for period in self.periods:
                line = period[0]+' '+period[1]+' \n'
                file.write(line)
            file.close()  
    def add_in_periods(self, periods, new_period):

        if len(periods) == 0:
            return [new_period]

        new_start, new_end = new_period['period']
        new_start = to_dat(new_start)
        new_end = to_dat(new_end)
        flag = True
        for i, period in enumerate(periods):
            period_start, period_end = period['period']
            period_start = to_dat(period_start)
            period_end = to_dat(period_end)
            if new_end < period_start:
                flag = False
                periods[i:i] = [new_period]
                break
        if flag:
            periods.append(new_period)

        return periods
              
def to_dat(string_date):
    return datetime.strptime(string_date, '%Y-%m-%d')

def to_str(dt_date):
    return dt_date.strftime('%Y-%m-%d')