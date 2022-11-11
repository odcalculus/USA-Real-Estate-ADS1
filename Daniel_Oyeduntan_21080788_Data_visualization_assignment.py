#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 18:46:54 2022

@author: danieloyeduntan
"""

#As we begin our analysis, we need to import the necessary libraries (Pandas, Numpy and Matplotlib)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#We will also need to import the urllib library to help download our file
from urllib.request import urlretrieve
link_to_page = 'https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset?select=realtor-data.csv'
#please note that due to kaggle's API structure, the download link might have expired as at when this program is reran 
download_link = 'https://storage.googleapis.com/kaggle-data-sets/2218738/4063426/compressed/realtor-data.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221110%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221110T113528Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=8bdf734d27b12aabe8f7c30cd6b60a0eb57db333e8d7e226846f2729904b94e108796a215c5df83c32224e3e2e15686ed06ede60277104edd7cca951a3ccb14b0ebf9b1eba06b3b889cf26f9380c30511162419bc80018840fb83d49a27369f274ec4658ea8144d87186631420f86ece65ae0dea9c6670a3ecaa971d49877b193b18962e6d86bde78f4482a5f7033f83b77a7bfce41215b09a7833cb6bf1d9c5d9c9f20f9c87d2660b1c2c9f1b22d29daf137abbedb27f3f6ce5c7fa6ebefebb155cc3a6f03458eacca1267ff42f8580f9fed3253e5669df46bf25578edd3d6fb3d35b0c5cc8cbcdfaf0e3eef103f8b2d1e7df563544aa0dcc293ef092565ee4'
urlretrieve(download_link, 'realtor-data.csv.zip')

#Our file was downloaded as a zip file so we need to import a new library called 'zipfile' to help extract it
import zipfile

#For the purpose of this analysis, we would define some functions (i.e. a group of related statements that performs a specific task). As we proceed in the analysis, we would be calling and using them.

#1. A function that produces a dataframe showing the number of missing values in each column of the dataframe passed. The function takes one argument which is the dataframe
def nan_dataframe(dataframe):
    nan_list = []
    for i in range(len(dataframe.columns)):
        nan_list.append(dataframe[dataframe.columns[i]].isna().sum())
    nan_df = pd.DataFrame([nan_list],["No. of missing values"], columns = df.columns)   
    return nan_df

#2. A function that produces a new dataframe after dropping all missing values from all columns or specified columns. It takes one or two argument - the first one being the dataframe and second(optional) is the specific columnn that we want to drop from
def drop_nan(df,column = ""):
    if column == "":
        updated_df = df.dropna()
        return updated_df
    else:
        updated_df = df[df[column].notna()]
        return updated_df

#3. A function that groups or summarizes dataframe by methods and given criterias. The function takes 4 arguments - the dataframe, the columnns we want to group by, a list of columns we want grouped and the method of grouping
def group_by(dataframe,groupby_column,grouped_columns_list,group_method):
    if group_method == 'sum':
        new_grouped_dataframe = dataframe.groupby(groupby_column)[grouped_columns_list].sum()
        return new_grouped_dataframe
    elif group_method == 'mean':
        new_grouped_dataframe = dataframe.groupby(groupby_column)[grouped_columns_list].mean()
        return new_grouped_dataframe
    elif group_method == 'count':
        new_grouped_dataframe = dataframe.groupby(groupby_column)[grouped_columns_list].count()
        return new_grouped_dataframe
    elif group_method == 'median':
        new_grouped_dataframe = dataframe.groupby(groupby_column)[grouped_columns_list].median()
        return new_grouped_dataframe
    elif group_method == 'min':
        new_grouped_dataframe = dataframe.groupby(groupby_column)[grouped_columns_list].min()
        return new_grouped_dataframe
    elif group_method == 'max':
        new_grouped_dataframe = dataframe.groupby(groupby_column)[grouped_columns_list].max()
        return new_grouped_dataframe
    elif group_method == 'mode':
        new_grouped_dataframe = dataframe.groupby(groupby_column)[grouped_columns_list].mode()
        return new_grouped_dataframe
    elif group_method == 'std':
        new_grouped_dataframe = dataframe.groupby(groupby_column)[grouped_columns_list].std()
        return new_grouped_dataframe
    elif group_method == 'var':
        new_grouped_dataframe = dataframe.groupby(groupby_column)[grouped_columns_list].var()
        return new_grouped_dataframe
    else:
        print('This function is not able to group your dataframe by the method given')
    
#4 A function that prints a table of the description of the dataframe passed into it and plots an histogram of all numeric columns. This functions has only one argument which is the dataframe.
def des_hist(dataframe):
    describe = dataframe.describe()
    print('Below is a table that shows a brief description of the passed in dataframe')
    print(describe)
    x = len(describe.columns)
    plt.figure(figsize=(x*3.5,5))
    for i in range(x):
        plt.subplot(1,x,1+i).set_title(describe.columns[i],fontsize=8)
        plt.hist(dataframe[describe.columns[i]].dropna(),bins=100)
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=6)
    plt.show()
    
#5 A function that plots a subplots of bar charts. This functions takes 3 arguments - the x axis, a list of y axis and a corresponding list of labels
def bar_chart_subplot(x_axis,my_list,labels):
    x = len(my_list)
    plt.figure(figsize=(x*5.5,8),edgecolor='black')
    for i in range(x):
        plt.subplot(1,x,1+i).set_title(labels[i],fontsize=10)
        plt.bar(x_axis,my_list[i])
        plt.yticks(fontsize=6)
        plt.xticks(fontsize=10,rotation=90)
    plt.show()
        
#6 A function that produces scattar plots of variables in a list, each plotted against every other variable. This functions takes two arguments - a list of arrays to be plotted and the corresponding labels
def scatter_plot(my_list,label):
    x_list = y_list = my_list
    x = len(x_list)
    y = len(y_list)
    for i in range(x):
        plt.figure(figsize=(x*5,6))
        for j in range(y):
            plt.subplot(1,y,1+j)
            plt.scatter(x_list[i],y_list[j])
            plt.xlabel(label[i])
            plt.ylabel(label[j])
            plt.yticks(fontsize=6)
            plt.xticks(fontsize=7)
        plt.show()
    
#7 A function to plot multiple line graph. This function takes 4 arguments - the common x axis, a list of y axis to be plotted, a corresponding list of labels for the y-axis and the x-axis label.
def line_plot(x_axis,y_axis,y_label,x_label):
    x = len(y_axis)
    plt.figure(figsize=(8,4))
    for i in range(x):
        plt.plot(x_axis,y_axis[i],label=y_label[i])
    plt.xticks(fontsize=7)
    plt.yticks(fontsize=6)
    plt.legend()
    plt.xlabel(x_label)
    plt.show()

#We would now read the file to pandas using the following lines of code
zf = zipfile.ZipFile('realtor-data.csv.zip') 
df = pd.read_csv(zf.open('realtor-data.csv'))

#We want to take a quick look at our data. To do that we will be calling the 'des_hist' function previously defined
des_hist(df)

#Now we want to clean and preprocess our data. First thing we need to do is check the columns will NaN values; to do that we will create a dataframe that will show us the number of NaN in each column. To do that we will be calling the 'nan_dataframe' function previously defined
nan_df = nan_dataframe(df)
print(nan_df)
print()
#The next thing to will be to deal with the missing values, we will drop all rows with missing values. To do that we will be calling the 'drop_nan' function previously defined
df2 = drop_nan(df)

#Moving forward, we will continue our analysis with df2

#After cleaning, we will once again check our new dataframe. To do that we will be calling the 'des_hist' function previously defined
des_hist(df2)

#Now we want to find get a summary table of the averages of price, bed, bath, acre_lot and house_size. To do that we will be calling the 'group_by' function previously defined
my_list = ['price','bed','bath','acre_lot','house_size']
state_avg = group_by(df2,'state',my_list,'mean')
print(state_avg)
print()

#We will now plot a bar charts representing the summary table of all states. To do that we will be calling the 'bar_chart_subplot' function previously defined
x_axis = state_avg.index
my_list = [state_avg['price'],state_avg['bed'],state_avg['bath'],state_avg['acre_lot'],state_avg['house_size']]
labels = ['Price','Bed','Bath','Acre_lot','House_size']
bar_chart_subplot(x_axis,my_list,labels)

#As we all know, the prices of houses are majorly determined by a number of variables some of which are number of rooms, number of batherooms, the acre lot size, the size of the house. We want to test that theory with this dataset by creating a correlation table of 'Price' and other numeric variables and also plottong a scatter plot. To do that we will be calling the 'scatter_plot' function previously defined
print(df2.corr())
print()
my_list = [df2['price'],df2['bed'],df2['bath'],df2['acre_lot'],df2['house_size']]
label = ['Price','Bed','Bath','Acre_lot','House_size']
scatter_plot(my_list,label)

#The next analysis we want to do is to check the trend over the years of prices, number of bedroom, number of bathroom, acre lot and house size. We then define a new dataframe to slice out unwanted columns, then create a new column called 'year'
df3 = df2[['price','bed','bath','acre_lot','house_size','sold_date']]
df3['date'] = pd.to_datetime(df3['sold_date'])
df3['year'] = pd.DatetimeIndex(df3['date']).year

#Then we do a summary table of averages grouping by year using the 'group_by' function previously defined
my_list = ['price','bed','bath','acre_lot','house_size']
sold_year_group = group_by(df3,'year',my_list,'mean')
print(sold_year_group)
print()

#Finally we plot a line graph using the 'line_graph' function previously defined to check for YoY trend. For clarity, we will plot for Price aand House_size individually because of the desparity in size of variables comapred to other features; then we do a multiple plot for Bed, Bath, Acre_lot.

#Line graph for price only
x_axis = sold_year_group.index
y_axis = [sold_year_group['price']]
label = ['price']
x_label = 'Year'
line_plot(x_axis,y_axis,label,x_label)

#Line graph for house_size only
x_axis = sold_year_group.index
y_axis = [sold_year_group['house_size']]
label = ['house_size']
x_label = 'Year'
line_plot(x_axis,y_axis,label,x_label)

#Line graph for bed,bath and acre_lot
x_axis = sold_year_group.index
y_axis = [sold_year_group['bed'],sold_year_group['bath'],sold_year_group['acre_lot']]
label = ['bed', 'bath', 'acre_lot']
x_label = 'Year'
line_plot(x_axis,y_axis,label,x_label)

