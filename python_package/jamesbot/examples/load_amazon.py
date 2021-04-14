from jamesbot import *

dl = DataLoader()
dl.load('AMZN','2019-01-01', '2020-05-01')
dl.load('AMZN','2019-01-01', '2020-05-01')
dl.load('AMZN','2020-07-01', '2021-03-01')
dl.load('AMZN','2015-07-01', '2016-03-01')
df = dl.load('AMZN','2014-07-01', '2021-04-01')

print(df)

