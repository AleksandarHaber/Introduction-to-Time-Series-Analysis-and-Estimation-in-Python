# -*- coding: utf-8 -*-
"""
Intro to time series analysis in Python
Created on Fri Jan  1 21:05:29 2021

@author: Aleksandar Haber

"""
# standard imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# statsmodels libraries
import statsmodels.api as sm

# set for reproducibility
np.random.seed(1)



###########################################################################################
#                                WHITE NOISE 
###########################################################################################
# number of time samlpes
time_samples=5000

time_series=np.random.normal(size=time_samples)

# plot the generated time series
plt.figure(figsize=(10,5))
plt.plot(time_series[0:1000])
plt.savefig('white_noise.png')

time_series_pd = pd.Series(time_series)

# autocorrelation plot
# https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html
# https://www.statsmodels.org/devel/generated/statsmodels.tsa.stattools.acf.html
# https://stackoverflow.com/questions/28517276/changing-fig-size-with-statsmodel

with mpl.rc_context():
    mpl.rc("figure",figsize=(12,8))  # here adjust the figure size
    sm.graphics.tsa.plot_acf(time_series_pd, lags=40)
    plt.savefig('acf_random.png')

# store the numerical values in vectors
# alpha - confidence interval    
# see also 
# https://stackoverflow.com/questions/61855401/statsmodels-pacf-plot-confidence-interval-does-not-match-pacf-function    
acf_random, acf_random_confidence = sm.tsa.stattools.acf(time_series_pd,nlags=40, alpha=0.05)



# partial autocorrelation plot 
# https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_pacf.html
# https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.pacf.html

with mpl.rc_context():
    mpl.rc("figure",figsize=(12,8))  # here adjust the figure size
    sm.graphics.tsa.plot_pacf(time_series_pd, lags=40)
    plt.savefig('pacf_random.png')

# store the numerical values in vectors
# alpha - confidence interval
pacf_random, pacf_random_confidence = sm.tsa.stattools.pacf(time_series_pd,nlags=40, alpha=0.05)


# QQ plot
# https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.qqplot.html


with mpl.rc_context():
    mpl.rc("figure",figsize=(12,8))  # here adjust the figure size
    sm.qqplot(time_series_pd,line='s')
    plt.title('QQ plot')
    plt.savefig('QQ_random.png')

###########################################################################################



###########################################################################################
#                       AR(1) plot                                   
###########################################################################################
# generate AR(1) series

# number of time sampes
time_samples=5000

# coefficient 
ar_coeff=0.8

time_series_ar=np.random.normal(size=time_samples)

for i in range(time_samples-1):
    time_series_ar[i+1]=ar_coeff*time_series_ar[i]+np.random.normal()

# plot the generated time series
plt.figure(figsize=(10,5))
plt.plot(time_series_ar[0:1000])
plt.savefig('ar_process.png')
time_series_ar_pd = pd.Series(time_series_ar)

# autocorrelation plot
# https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html
# https://www.statsmodels.org/devel/generated/statsmodels.tsa.stattools.acf.html

with mpl.rc_context():
    mpl.rc("figure",figsize=(12,8))  # here adjust the figure size
    sm.graphics.tsa.plot_acf(time_series_ar_pd, lags=40)
    plt.savefig('acf_ar.png')

# store the numerical values in vectors
# alpha - confidence interval    
acf_ar, acf_ar_confidence = sm.tsa.stattools.acf(time_series_ar_pd,nlags=40, alpha=0.05)

# partial autocorrelation plot 
# https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_pacf.html
# https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.pacf.html

with mpl.rc_context():
    mpl.rc("figure",figsize=(12,8))  # here adjust the figure size
    sm.graphics.tsa.plot_pacf(time_series_ar_pd, lags=40)
    plt.savefig('pacf_ar.png')

# store the numerical values in vectors
# alpha - confidence interval
pacf_ar, pacf_ar_confidence = sm.tsa.stattools.pacf(time_ar_pd,nlags=40, alpha=0.05)


# QQ plot
# https://www.statsmodels.org/stable/generated/statsmodels.graphics.gofplots.qqplot.html

with mpl.rc_context():
    mpl.rc("figure",figsize=(12,8))  # here adjust the figure size
    sm.qqplot(time_series_ar_pd,line='s')
    plt.title('QQ plot')
    plt.savefig('QQ_ar.png')
    
# test - take the difference 
# https://numpy.org/doc/stable/reference/generated/numpy.diff.html
    
time_series_ar_diff=np.diff(time_series_ar)
time_series_ar_diff_pd = pd.Series(time_series_ar_diff)

with mpl.rc_context():
    mpl.rc("figure",figsize=(12,8))  # here adjust the figure size
    sm.graphics.tsa.plot_acf(time_series_ar_diff_pd, lags=40)
    plt.savefig('acf_ar_diff.png')



###########################################################################################    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
