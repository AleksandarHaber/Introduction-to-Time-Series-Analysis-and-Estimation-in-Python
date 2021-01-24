# -*- coding: utf-8 -*-
"""
Intro to time series analysis in Python 

Pandas Series and DataFrame structures demonstration - Advanced Topics I 


@author: Aleksandar Haber
Date: January 04, 2021
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

import datetime #necessary for creating a datetime object
import pandas_datareader as pdr #necessary for downloading the stock data from Yahoo! Finance
# you need to install this library by opening a command line and by typing "pip install pandas-datareader"


# load the stock data from internet

start_time=datetime.datetime(2020,1,1)
end_time=datetime.datetime(2021,1,1)

# load the Amazon stock data 
amzn=pdr.get_data_yahoo('AMZN', start=start_time, end=end_time)

# load the Boeing stock data 
ba=pdr.get_data_yahoo('BA', start=start_time, end=end_time)

# another way for defining the time stamps - using the pd.Timestamp() function

amzn2=pdr.get_data_yahoo('AMZN', pd.Timestamp('2020,01,01'), pd.Timestamp('2021,01,01'))
ba2=pdr.get_data_yahoo('BA', pd.Timestamp('2020,01,01'), pd.Timestamp('2021,01,01'))

# investigate the data

amzn.head()

# get the index timestamps
amzn.index

# get the column names
amzn.columns

# plot the values at the rows 1,2,3
amzn.values[0:3,:]

# you can for example store the values in a numpy array for further processing

amzn_values=amzn.values
amzn_values

# compute basic statistics 
amzn.describe()

#plot the closing prices
ax1=amzn['Adj Close'].plot(figsize=(10,5),title='Amazon stock historical price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Closing price')
# save the figure to a file
plt.savefig('amzn.png')

#plot the closing prices
ax2=ba['Adj Close'].plot(figsize=(10,5),title='Boeing stock historical price')
ax2.set_xlabel('Date')
ax2.set_ylabel('Closing price')
# save the figure to a file
plt.savefig('ba2.png')

# plot the trading volume
amzn['Volume'].plot(figsize=(10,5))

# save data to a file 
amzn.to_csv('amzn_data.csv')

# load data from the saved file 
loaded_amzn=pd.read_csv('amzn_data.csv')

loaded_amzn['Adj Close'].plot(figsize=(10,5))

# resample the data 
monthly_resampled_amzn=amzn['Adj Close'].resample('M').mean()

monthly_resampled_amzn

monthly_resampled_amzn.plot()


# add a new column to data that is difference


amzn['diff']=amzn['Open']-amzn['Close']

amzn.columns
amzn.head()
amzn['diff'].plot()

# delete a column 

del amzn['diff']

amzn.columns


#concatenate 

close_amzn=amzn['Adj Close']
close_ba=ba['Adj Close']

close_concat=pd.concat([close_amzn,close_ba],axis=1)

close_concat.head()

close_concat.columns

# concatenate everything

concat=pd.concat([amzn,ba], axis=1)

concat.head()

concat.columns



# another way for concatenating by using keys

concat2=pd.concat([amzn,ba], axis=1, keys=['AMZN','BA'])

# acessing the entries
concat2.head()

concat2['AMZN'].head()

concat2['AMZN']['Adj Close'].head()

concat2['AMZN']['Adj Close'].loc['2020-01-02']



