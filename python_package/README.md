
# JamesBot     ![](https://ibb.co/K26CH92) 

My name is Bot, I'm a [James](https://github.com/felipe-fp/JamesBot).

JamesBot is a python package that downloads and retains financial data from Yahoo Finance API and Bloomberg API, making possible to load financial time series previously loaded locally.


## Installation


Install JamesBot package using **pip**:
```
 pip install jamesbot --upgrade
```

## How to use


```python
from jamesbot import *

dl = DataLoader() # creates DataLoader
df = dl.load('AMZN','2014-07-01', '2021-04-01') # loads Amazon's stock price 

print(df) # prints DataFrame

```

## Bloomberg API

If you have a Bloomberg API License, it is also possible to load data from it. When getting data, 
you must have Bloomberg's Terminal open in your machine.

p.s: Note that Bloomberg ticker's names must include the market's name.

```python
from jamesbot import *

dl = DataLoader(source='bloomberg') # creates DataLoader
df = dl.load('AMZN US Equity','2014-07-01', '2021-04-01') # loads Amazon's stock price 

print(df) # prints DataFrame

```

