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
import matplotlib.pyplot as plt

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
print("The names of 3-cylinders cars are:", end=" ")
for x in carname_3: print(x, end=" | ")

# 3. What is the range, mean, and standard deviation of each attribute? Pay attention to potential
# missing values
print("\n\n3.")
data = data.dropna()

drop_list = ['count', 'min', '25%', '50%', '75%', 'max']
attribute_list = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'model', 'origin']

def add_range(df):
    df1 = df.describe()
    df1.loc["range"] = df1.loc['max'] - df1.loc['min']
    return df1

for x in attribute_list:
    print("\nMean, standard deviation and range of", x)
    tmp = add_range(data[x])
    tmp = tmp.drop(labels= drop_list)
    print(tmp)

# 4. Plot histograms for each attribute. Pay attention to the appropriate choice of number of bins.
# Write 2-3 sentences summarizing some interesting aspects of the data by looking at the histograms
print("\n4.")

n_bins = []


# for x in attribute_list:
#     tmp = data[x].describe()
#     #h = 2 * (tmp.loc['75%'] - tmp.loc['25%']) * tmp.loc['count']**(-1/3)
#     n_bins.append((tmp.loc['max']-tmp.loc['min']))

# print(n_bins)

# for x in attribute_list:
#     fig_obj = plt.figure(figsize=(10, 7.5))
#     ''' Place an 2-D axis system on the Canvas '''
#     ax = plt.subplot(111)
#     ax.spines["bottom"].set_visible(True)  # Set the spines, or box bounds visibility
#     ax.spines["left"].set_visible(True)    
#     ax.spines['right'].set_visible(False)
#     ax.spines['top'].set_visible(False)
#     ''' Plot the histogram of '''
#     p = plt.hist(data[x], bins = 30)
#     plt.title(x, fontsize=14, fontweight='bold')
#     ''' Save figure '''
#     plt.tight_layout()
#     plt.savefig('./pics/'+x+'_histogram.png', bbox_inches='tight')

# # 5. 
# for x in attribute_list:
#     data[x]=data[x] + np.random.random(len(data[x]))

print(data['mpg'].min())


print(data.shape)