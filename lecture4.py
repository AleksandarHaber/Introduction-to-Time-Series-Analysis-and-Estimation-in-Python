# -*- coding: utf-8 -*-
"""
Moving average of stock prices 
Author:
    Aleksandar Haber
Date: January 21, 2021
Some parts of this code are inspired by the codes given in 
"Learn Algorithmic Trading: Build and deploy algorithmic trading systems and strategies
using Python and advanced data analysis"

by Sebastien Donadio and Sourav Ghosh
"""
# simple moving average implementation in Python and comparison with Pandas 

# standard imports
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# used to donwload the stock prices
import pandas_datareader as pdr

#necessary for computing averages
import statistics as stats

# define the parameters

moving_average_window=40


# define the dates for downloading the data

startDate= '2016-01-01 '
endDate= '2021-01-01'

# Read about Python pickle file format:  https://www.datacamp.com/community/tutorials/pickle-python-tutorial
fileName = 'downloadedData.pkl'

stock_symbol='AAPL'

# this piece of code either reads the data from the saved file or if the saved file does not exist 
# it downloads the data 

try:
    data=pd.read_pickle(fileName)
    print('Loading the data from the local disk.')
except FileNotFoundError:
    print('The data is not found on the local disk.')
    print('Downloading the data from Yahoo.')
    data = pdr.get_data_yahoo(stock_symbol,start=startDate,end=endDate)
    # save the data to file
    print('Saving the data to the local disk.')
    data.to_pickle(fileName)

# inspect the data
    
data.head()

data['Adj Close'].plot()

# isolate the closing price

closingPrice = data['Adj Close']

# isolate the values
closingPrice.values

# computed moving averages
computedMovingAverages=[]

batch=[]


for price in closingPrice.values:
    batch.append(price)
    # if the number of stored entries is larger than the batch capacity, erase the 
    # first entry
    if len(batch) > moving_average_window:
        del(batch[0])
        
    computedMovingAverages.append(stats.mean(batch))
    
# append the original data frame with the computed moving average
# that is, add a column that will contain the values of the computed moving averages

data=data.assign(Moving_average=pd.Series(computedMovingAverages,index=data.index))

#plot the results

fig1=plt.figure(figsize=(10,8))
ax1=fig1.add_subplot(111,ylabel='Stock price [$]')
data['Adj Close'].plot(ax=ax1, color='b', lw=3, legend=True)
data['Moving_average'].plot(ax=ax1, color='r', lw=3, legend=True )
plt.savefig('moving_average.png')
plt.show()
    
    
# check the result using the pandas function

moving_average_pandas=data['Adj Close'].rolling(window=moving_average_window).mean()

moving_average_pandas

data['Moving_average']


#compare the results 

fig2=plt.figure(figsize=(10,8))
ax2=fig2.add_subplot(111,ylabel='Moving averages [$]')
data['Moving_average'].plot(ax=ax2, color='r', lw=10, label='Manually computed', legend = True )
moving_average_pandas.plot(ax=ax2, color='k', lw=3, label='Pandas rolling function',  legend = True)
plt.savefig('moving_average_comparison.png')
plt.show()




