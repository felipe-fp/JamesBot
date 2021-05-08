from data_loader import DataLoader

dl = DataLoader(source='bloomberg')

dl.load('AMZN US Equity','2019-01-01', '2020-05-01')
df = dl.load('AMZN US Equity','2019-01-01', '2020-05-01')
dl.load('AMZN US Equity','2020-07-01', '2021-03-01')
dl.load('AMZN US Equity','2015-07-01', '2016-03-01')
dl.load('AMZN US Equity','2014-07-01', '2021-04-01')

print(df)
