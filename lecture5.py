# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import statistics

data = [3,4,5,6,7]
avg = statistics.mean(data)
med = statistics.median(data)
#mod = statistics.mode(data)
sd = statistics.stdev(data)
var = statistics.variance(data)

data2 = [1,2,5,8,9]


import numpy as np
import pandas
import matplotlib.pyplot as plt
x = np.array([0,1,3,5,10,15,20]) #t_day
y = np.array([12,10.7,9,7.1,4.6,2.5,1.8])  #conc_mg_per_L

#create a dataframe containing concentration versus time data
data = pandas.DataFrame({'x': x, 'y': y})
from statsmodels.formula.api import ols
model = ols("y ~ x", data).fit()
print(model.summary())

#Constructing linear model for first order reaction (model2) 