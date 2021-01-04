# -*- coding: utf-8 -*-
"""
Intro to time series analysis in Python 

Pandas Series and DataFrame structures demonstration


@author: Aleksandar Haber
Date: January 03, 2021
"""
import pandas as pd 
import numpy as np

###############################################################################
#                   The Series Pandas structure
###############################################################################

# Create a simple random series
random_array=np.random.randn(10)
series=pd.Series(random_array)
print(series)

# series consists of an index and a sequence of values 
print(series.index)
print(series.values)

# create series by specifying values and by labeling the indices
series2=pd.Series([10,20,30,40], index=['i1','i2','i3','i4'])

print(series2)

# create series from dictionaries - keys of dictionary are used as index labes

dict1={'i1':10, 'i2':20, 'i3':30, 'i4':40}
series3=pd.Series(dict1)

#indexing 
series[0]
series[1]
series[2]

#multiple value indexing
series[[0, 1, 2]]

# slice notation - similar to MATLAB 
series[0:3]

# beginning and end 
series.head()
series.tail()

# length, shape, number of elements, etc. 

len(series)
series.shape
series.count()

#construct a time series with repeated entries 

series4=pd.Series(np.array([1,1,1,2]))

# count only entries that do not repeat
series4.unique()

# alignment via index labels

series5=pd.Series([1,2,3], index=['i1','i2','i3'])

series6=pd.Series([5,6,7], index=['i2','i3','i1'])

series7=series5+series6

series7
###############################################################################
#                 end of the Series Pandas structure
###############################################################################


###############################################################################
#                   The DataFrame Pandas structure
###############################################################################

# create a DataFrame structure from a NumpyArray
# index and column names are automatically assigned

frame1=pd.DataFrame(np.array([[1,2],[3,4]]))
frame1

#construction from a list of Series objects
seriesList1=[pd.Series([1,2,3,4]),pd.Series([5,6,7,8])]
dataFrame1=pd.DataFrame(seriesList1)
dataFrame1

#shape
dataFrame1.shape

#specify the column names while creating the DataFrame

dataFrame2=pd.DataFrame(np.array([[1,2],[3,4]]), columns=['a','b'])

dataFrame2

#access the column names

dataFrame2.columns

#change the column names
dataFrame2.columns = ['c1','c2']

dataFrame2

#specify the column names and index labels while creating the DataFrame

dataFrame3=pd.DataFrame(np.array([[10,20],[30,40]]),
                        columns=['c1','c2'],index=['r1','r2'])

dataFrame3

# access the index values 

dataFrame3.index

# get the matrix values

dataFrame3.values


# selecting the columns, values, rows, etc. 

# construct a DataFrame
dataFrame4=pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),
                    columns=['c1','c2','c3'],
                    index=['r1','r2','r3'])

# select the second column
dataFrame4['c2']

# another way
dataFrame4.c2

#select two columns at the same time 
dataFrame4[['c1','c2']]


# row selection 

# select the first two rows
dataFrame4[:2]

dataFrame4['r1':'r2']

# explicitly select the row by specifying the index label 

dataFrame4.loc['r1']

dataFrame4.iloc[0]

# two rows at the same time 

dataFrame4.loc[['r1','r2']]

dataFrame4.iloc[[0,1]]


# scalar lookup at the values at certain locations

dataFrame4.at['r2','c2']

dataFrame4.iat[1,1]