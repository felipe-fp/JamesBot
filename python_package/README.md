
# JamesBot     ![](https://ibb.co/K26CH92) 

My name is Bot, I'm a [James](https://github.com/felipe-fp/JamesBot).

JamesBot is a python package that downloads and retains financial data from Yahoo Finance API, making possible to load financial time series previously loaded locally.


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

