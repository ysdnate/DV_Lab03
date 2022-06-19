# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
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
    return '1_' + cell[0] + cell[1]
a.Hour = a.Hour.apply(getHour_1)

b = data[data.Date == '2/2/2007']
b['Hour'] = b.Time.str.split(':')
def getHour_2(cell):
    return '2_' + cell[0] + cell[1]
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
    plt.plot(temp.index, temp.Global_active_power, color="black")
    plt.tight_layout()
    positions = ('1_0000', '2_0000', '2_2359')
    labels = ('Thu', 'Fri', 'Sat')
    plt.xticks(positions, labels)
    plt.ylabel("Global Active Power (kilowatts)")
    plt.savefig("./pics/plot2.png", bbox_inches="tight")
    plt.close()

plot2()

def plot3():
    fig_obj = plt.figure(figsize=(10, 7.5))
    ax = plt.subplot(111)
    ax.spines["bottom"].set_visible(True)  # Set the spines, or box bounds visibility
    ax.spines["left"].set_visible(True)    
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    x = df.Hour
    y1 = df.Sub_metering_1
    y2 = df.Sub_metering_2
    y3 = df.Sub_metering_3
    df_2 = pd.concat([x,y1,y2,y3], axis=1)
    temp = df_2.groupby("Hour").sum()
    plt.plot(temp.index, temp.Sub_metering_1, color="black")
    plt.plot(temp.index, temp.Sub_metering_2, color="red")
    plt.plot(temp.index, temp.Sub_metering_3, color="blue")
    plt.legend(["Sub_metering_1","Sub_metering_2","Sub_metering_3"], bbox_to_anchor=(1, 1), loc=1, borderaxespad=0)
    plt.tight_layout()
    positions = ('1_0000', '2_0000', '2_2359')
    labels = ('Thu', 'Fri', 'Sat')
    plt.xticks(positions, labels)
    plt.ylabel("Energy sub metering")
    plt.savefig("./pics/plot3.png", bbox_inches="tight")
    plt.close()
    
plot3()

def voltage_plot():
    fig_obj = plt.figure(figsize=(10, 7.5))
    ax = plt.subplot(111)
    ax.spines["bottom"].set_visible(True)  # Set the spines, or box bounds visibility
    ax.spines["left"].set_visible(True)    
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    x = df.Hour
    y = df.Voltage
    df_2 = pd.concat([x,y], axis=1)
    temp = df_2.groupby("Hour").sum()
    plt.plot(temp.index, temp.Voltage, color="black")
    plt.tight_layout()
    positions = ('1_0000', '2_0000', '2_2359')
    labels = ('Thu', 'Fri', 'Sat')
    plt.xticks(positions, labels)
    plt.ylabel("Voltage")
    plt.savefig("./pics/voltage.png", bbox_inches="tight")
    plt.close()

voltage_plot()

def reactive_plot():
    fig_obj = plt.figure(figsize=(10, 7.5))
    ax = plt.subplot(111)
    ax.spines["bottom"].set_visible(True)  # Set the spines, or box bounds visibility
    ax.spines["left"].set_visible(True)    
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    x = df.Hour
    y = df.Global_reactive_power
    df_2 = pd.concat([x,y], axis=1)
    temp = df_2.groupby("Hour").sum()
    plt.plot(temp.index, temp.Global_reactive_power, color="black")
    plt.tight_layout()
    positions = ('1_0000', '2_0000', '2_2359')
    labels = ('Thu', 'Fri', 'Sat')
    plt.xticks(positions, labels)
    plt.ylabel("Global_reactive_power")
    plt.savefig("./pics/reactive.png", bbox_inches="tight")
    plt.close()

reactive_plot()

def plot4():
    
    fig = plt.figure(figsize=(40, 30))
    rows = 2
    columns = 2
    Image1 = cv2.imread('./pics/plot2.png')
    Image2 = cv2.imread('./pics/voltage.png')
    Image3 = cv2.imread('./pics/plot3.png')
    Image4 = cv2.imread('./pics/reactive.png')
    
    fig.add_subplot(rows, columns, 1)
    plt.axis('off')
    plt.imshow(Image1)

    fig.add_subplot(rows, columns, 2)
    plt.axis('off')
    plt.imshow(Image2)

    fig.add_subplot(rows, columns, 3)
    plt.axis('off')
    plt.imshow(Image3)

    fig.add_subplot(rows, columns, 4)
    plt.axis('off')
    plt.imshow(Image4)
    
    plt.savefig("./pics/plot4.png", bbox_inches="tight")
    plt.close()

plot4()

