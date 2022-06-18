# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 21:53:34 2015

@author: nymph
"""


#################################### Read the data ############################
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns
import numpy as np

''' read_csv()
The read_csv() function in pandas package parse an csv data as a DataFrame data structure. What's the endpoint of the data?
The data structure is able to deal with complex table data whose attributes are of all data types. 
Row names, column names in the dataframe can be used to index data.
'''

data = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original", delim_whitespace = True, \
 header=None, names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model', 'origin', 'car_name'])

data['mpg']
data.mpg
data.iloc[0,:]

#print(data.shape)
#print(data.head())
################################## Enter your code below ######################

# 1. How many cars and how many attributes are in the data set?
print("1. There are", data.shape[0], "cars and", data.shape[1], "attributes in the data set." )

# 2. How many distinct car companies are represented in the data set? What is the name of the car
# with the best MPG? What car company produced the most 8-cylinder cars? What are the names
# of 3-cylinder cars? Do some internet search that can tell you about the history and popularity of
# those 3-cylinder cars.
print("2.")

data = data.assign(company = data['car_name'].str.split(' ',n=1, expand=True)[0])
print("There are",data.nunique()['company'],"distinct car companies in the data set.")

max_mpg = data[data['mpg']==data['mpg'].max()].car_name
print("The name of the car with the best MPG is",max_mpg.values)

cyl_8 = data[data['cylinders']==8]
count_8 = cyl_8.company.value_counts()
print("The company produced the most 8-cylinder cars is", count_8.index[0])

cyl_3 = data[data['cylinders']==3]
carname_3 = cyl_3.car_name
print("The names of 3-cylinders cars are:",carname_3.values)

# 3. What is the range, mean, and standard deviation of each attribute? Pay attention to potential
# missing values
data = data.dropna()
print("3.")
print("")
print(data["mpg"].describe())