# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""

from cProfile import label
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

############################## Your code for loading and preprocess the data ##
data = pd.read_csv('./data/household_power_consumption.txt', sep=';', header=0)

data.replace('?', np.nan, inplace=True)
data = data.dropna()

cols_change = data.columns[2:]

for x in cols_change:
    data[x] = data[x].astype(float)


a = data[data.Date == '1/2/2007']
a['Hour'] = a.Time.str.split(':')
def getHour_1(cell):
    return '1_' + cell[0]
a.Hour = a.Hour.apply(getHour_1)

b = data[data.Date == '2/2/2007']
b['Hour'] = b.Time.str.split(':')
def getHour_2(cell):
    return '2_' + cell[0]
b.Hour = b.Hour.apply(getHour_2)

df = pd.concat([a,b])



############################ Complete the following 4 functions ###############
def plot1():
    ''' Create a canvas with width 10, height 7.5 '''
    fig_obj = plt.figure(figsize=(10, 7.5))
    ''' Place an 2-D axis system on the Canvas '''
    ax = plt.subplot(111)
    ax.spines["bottom"].set_visible(True)  # Set the spines, or box bounds visibility
    ax.spines["left"].set_visible(True)    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ''' Plot the histogram of '''
    p = plt.hist(df.Global_active_power, bins = 19, color="red", edgecolor='black')
    plt.title("Global active power", fontsize=14, fontweight='bold')
    plt.xlabel("Global active power (kilowatts)")
    plt.ylabel("Frequency")
    
    ''' Save figure '''
    plt.tight_layout()
    plt.savefig('./pics/plot1.png', bbox_inches='tight')
    plt.show()
    plt.close()

plot1()

def plot2():
    fig_obj = plt.figure(figsize=(10, 7.5))
    ax = plt.subplot(111)

    ax.spines["bottom"].set_visible(True)  # Set the spines, or box bounds visibility
    ax.spines["left"].set_visible(True)    
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)

    x = df.Hour
    y = df.Global_active_power
    df_2 = pd.concat([x,y], axis=1)
    temp = df_2.groupby("Hour").sum()

    plt.plot(temp.index, temp.Global_active_power)
    plt.tight_layout()

    positions = ('1_00', '2_00', '2_23')
    labels = ('0h 1/2/2007', '0h 2/2/2007', '23h 2/2/2007')

    plt.xticks(positions, labels)


    plt.ylabel("Global Active Power (kilowatts)")

    plt.savefig("./pics/plot2.png", bbox_inches="tight")
    plt.show()
    plt.close()

plot2()

def plot3():
    pass

def plot4():
    pass

