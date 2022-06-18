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
print("\n2.")
data = data.assign(company = data['car_name'].str.split(' ',n=1, expand=True)[0])
print("There are",data.nunique()['company'],"distinct car companies in the data set.")

max_mpg = data[data['mpg']==data['mpg'].max()].car_name
print("The name of the car with the best MPG is",max_mpg.values[0])

cyl_8 = data[data['cylinders']==8]
count_8 = cyl_8.company.value_counts()
print("The company produced the most 8-cylinder cars is", count_8.index[0])

cyl_3 = data[data['cylinders']==3]
carname_3 = cyl_3.car_name
print("The names of 3-cylinders cars are:",carname_3.values)

# 3. What is the range, mean, and standard deviation of each attribute? Pay attention to potential
# missing values
print("\n3.")
data = data.dropna()
drop_list = ['count', 'min', '25%', '50%', '75%', 'max']

def add_range(df):
    df1 = df.describe()
    df1.loc["range"] = df1.loc['max'] - df1.loc['min']
    return df1

print("Mean, standard deviation and range of MPG:")
mpg_des = add_range(data["mpg"])
mpg_des = mpg_des.drop(labels= drop_list)
print(mpg_des)

print("\nMean, standard deviation and range of cylinders:")
cylinders_des = add_range(data["cylinders"])
cylinders_des = cylinders_des.drop(labels= drop_list)
print(cylinders_des)

print("\nMean, standard deviation and range of displacement:")
displacement_des = add_range(data["displacement"])
displacement_des = displacement_des.drop(labels= drop_list)
print(displacement_des)

print("\nMean, standard deviation and range of horsepower:")
horsepower_des = add_range(data["horsepower"])
horsepower_des = horsepower_des.drop(labels= drop_list)
print(horsepower_des)

print("\nMean, standard deviation and range of weight:")
weight_des = add_range(data["weight"])
weight_des = weight_des.drop(labels= drop_list)
print(weight_des)

print("\nMean, standard deviation and range of model:")
model_des = add_range(data["model"])
model_des = model_des.drop(labels= drop_list)
print(model_des)

print("\nMean, standard deviation and range of origin:")
origin_des = add_range(data["origin"])
origin_des = origin_des.drop(labels= drop_list)
print(origin_des)

# 4.