# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 10:37:52 2015

@author: shanshan
"""
################################################### Preprocessing ################################################

''' Import packages '''
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
#hihi
data['mpg']
data.mpg
data.iloc[0,:]

data = data.dropna()
''' describe()
Sometimes, describing the statistics of attributes is useful such as : mean, std, min, max, percentiles, etc. 
The describe() function can do this. It can be also combined with groupby() function to go deeper into the data.
'''

data.mpg.describe()
print(data.model.describe())
data.groupby(['cylinders']).mpg.describe()
''' pivot_table()
Sometimes, aggregation of values in different groups separated by different ways is interesting.
The pivot_table() function can specify the definition of groups, an attribute of interest and an aggregation function 
to perform on the attribute.
'''
pivot_table = data.pivot_table(index='cylinders', columns='acceleration', values='mpg', aggfunc=np.mean)
pivot_table.head()

############################################## Visualization #######################################################

''' Import the essential package 
matplotlib.pyplot is the most basic one.
seaborn enhances the visualization ability with statistical models.
plotly enables interactive ploting.
'''

import matplotlib.pyplot as plt
import seaborn as sns
#import plotly as py

''' Initial Plotting Parameters'''
plt.rcParams
rcDef = plt.rcParams
plt.rcParams.update(plt.rcParamsDefault)


''' Simple histogram '''
def hist_plot():
    ''' Create a canvas with width 10, height 7.5 '''
    fig_obj = plt.figure(figsize=(10, 7.5))
    ''' Place an 2-D axis system on the Canvas '''
    ax = plt.subplot(111)
    ax.spines["bottom"].set_visible(True)  # Set the spines, or box bounds visibility
    ax.spines["left"].set_visible(True)    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ''' Plot the histogram of '''
    p = plt.hist(data.mpg, edgecolor='black', bins = 30)
    plt.title("MPG", fontsize=14, fontweight='bold')
    
    ''' Save figure '''
    plt.tight_layout()
    plt.savefig('./pics/histogram.png', bbox_inches='tight')
    plt.show()

''' Scatter plot'''
def scatter_plot():
    ''' Create a canvas with width 10, height 7.5 '''
    fig_obj = plt.figure(figsize=(10, 7.5))
    ax = plt.subplot(111)
    
    p = plt.plot(data.mpg, data.weight, 'r.')
    plt.savefig('scatter1.png',bbox_inches='tight')
    plt.show()
    
def scatter_plot2():
    sns.lmplot("mpg", "weight", data, order=2);
    plt.savefig('scatter2.png',bbox_inches='tight')    
    plt.show()

def line_plot():

    ''' Read the data into a pandas DataFrame. '''
    gender_degree_data = pd.read_csv("http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv")  
    print(gender_degree_data)
    ''' These are the "Tableau 20" colors as RGB.  '''
    tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),  
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),  
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),  
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),  
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]  
      
    ''' Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts. '''
    for i in range(len(tableau20)):  
        r, g, b = tableau20[i]  
        tableau20[i] = (r / 255., g / 255., b / 255.)  
      
    ''' You typically want your plot to be ~1.33x wider than tall. This plot is a rare  
     exception because of the number of lines being plotted on it.  
     Common sizes: (10, 7.5) and (12, 9)'''
    fig_obj = plt.figure(figsize=(12, 14))  
      
    ''' Remove the plot frame lines. They are unnecessary chartjunk. ''' 
    ax = plt.subplot(111)  
    ax.spines["top"].set_visible(False)  
    ax.spines["bottom"].set_visible(False)  
    ax.spines["right"].set_visible(False)  
    ax.spines["left"].set_visible(False)  
      
    '''Ensure that the axis ticks only show up on the bottom and left of the plot.  
    # Ticks on the right and top of the plot are generally unnecessary chartjunk.  '''
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left()  
      
    '''# Limit the range of the plot to only where the data is.  
    # Avoid unnecessary whitespace.'''  
    plt.ylim(0, 90)  
    plt.xlim(1968, 2014)  
      
    '''# Make sure your axis ticks are large enough to be easily read.  
    # You don't want your viewers squinting to read your plot.  '''
    plt.yticks(range(0, 91, 10), [str(x) + "%" for x in range(0, 91, 10)], fontsize=14)  
    plt.xticks(fontsize=14)  
      
    '''# Provide tick lines across the plot to help your viewers trace along  
    # the axis ticks. Make sure that the lines are light and small so they  
    # don't obscure the primary data lines.  '''
    for y in range(10, 91, 10):  
        plt.plot(range(1968, 2012), [y] * len(range(1968, 2012)), "--", lw=0.5, color="black", alpha=0.3)  
          
    '''# Remove the tick marks; they are unnecessary with the tick lines we just plotted.  '''
    plt.tick_params(axis="both", which="both", bottom="off", top="off",  
                labelbottom="on", left="off", right="off", labelleft="on")  
      
    '''# Now that the plot is prepared, it's time to actually plot the data!  
    # Note that I plotted the majors in order of the highest % in the final year.  '''
    
    majors = ['Health Professions', 'Public Administration', 'Education', 'Psychology',  
          'Foreign Languages', 'English', 'Communications\nand Journalism',  
          'Art and Performance', 'Biology', 'Agriculture',  
          'Social Sciences and History', 'Business', 'Math and Statistics',  
          'Architecture', 'Physical Sciences', 'Computer Science',  
          'Engineering']  
    
    
    for rank, column in enumerate(majors):  
        '''# Plot each line separately with its own color, using the Tableau 20  
        # color set in order.  '''
        
        plt.plot(gender_degree_data.Year.values,  
                 gender_degree_data[column.replace("\n", " ")].values,  
                                    lw=2.5, color=tableau20[rank])  
           
        '''# Add a text label to the right end of every line. Most of the code below  
        # is adding specific offsets y position because some labels overlapped. ''' 
          
        y_pos = gender_degree_data[column.replace("\n", " ")].values[-1] - 0.5  
        if column == "Foreign Languages":  
            y_pos += 0.5  
        elif column == "English":  
            y_pos -= 0.5  
        elif column == "Communications\nand Journalism":  
            y_pos += 0.75  
        elif column == "Art and Performance":  
            y_pos -= 0.25  
        elif column == "Agriculture":  
            y_pos += 1.25  
        elif column == "Social Sciences and History":  
            y_pos += 0.25  
        elif column == "Business":  
            y_pos -= 0.75  
        elif column == "Math and Statistics":  
            y_pos += 0.75  
        elif column == "Architecture":  
            y_pos -= 0.75  
        elif column == "Computer Science":  
            y_pos += 0.75  
        elif column == "Engineering":  
            y_pos -= 0.25  
          
        '''# Again, make sure that all labels are large enough to be easily read  
        # by the viewer.  '''
        plt.text(2011.5, y_pos, column, fontsize=14, color=tableau20[rank])  
          
    '''# matplotlib's title() call centers the title on the plot, but not the graph,  
    # so I used the text() call to customize where the title goes.  
      
    # Make the title big enough so it spans the entire plot, but don't make it  
    # so big that it requires two lines to show.  
      
    # Note that if the title is descriptive enough, it is unnecessary to include  
    # axis labels; they are self-evident, in this plot's case.  '''
    
    
    plt.text(1995, 93, "Percentage of Bachelor's degrees conferred to women in the U.S.A., by major (1970-2012)", fontsize=17, ha="center")  
    
    plt.text(1966, -8, "Data source: nces.ed.gov/programs/digest/2013menu_tables.asp"  
       "\nAuthor: Randy Olson (randalolson.com / @randal_olson)"  
       "\nNote: Some majors are missing because the historical data "  
       "is not available for them", fontsize=10)  
      
    '''# Finally, save the figure as a PNG.  
    # You can also save it as a PDF, JPEG, etc.  
    # Just change the file extension in this call.  
    # bbox_inches="tight" removes all the extra whitespace on the edges of your plot.'''  
      
    plt.savefig("percent-bachelors-degrees-women-usa.png", bbox_inches="tight")
    plt.show()

line_plot()