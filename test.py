from stock import Stock

Amazon = Stock('AMZN')
df = Amazon.load('2019-01-01', '2020-05-01')
df = Amazon.load('2020-07-01', '2021-03-01')
df = Amazon.load('2015-07-01', '2016-03-01')
df = Amazon.load('2014-07-01', '2021-04-01')

print(df.head(3))
print((df.duplicated()).sum())
