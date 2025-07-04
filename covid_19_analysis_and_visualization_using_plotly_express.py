# -*- coding: utf-8 -*-
"""Covid-19 Analysis and Visualization using Plotly Express.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XirLBgLi3zlGG8Ck3QLabfNiIRFgmYVf

# Covid-19 Analysis and Visualization using Plotly Express

# Importing Necessary Libraries
"""

# Data analysis and Manipulation
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import pandas as pd

# Data Visualization
import matplotlib.pyplot as plt

# Importing Plotly
import plotly.offline as py
py.init_notebook_mode(connected=True)

# Initializing Plotly
pio.renderers.default = 'colab'

"""# Importing the Datasets"""

# Importing Dataset1
dataset1 = pd.read_csv("/content/covid.csv")
dataset1.head()  # returns first 5 rows

"""# getting dataset information"""

# Returns tuple of shape (Rows, columns)
print(dataset1.shape)

# Returns size of dataframe
print(dataset1.size)

# Information about Dataset1
# return concise summary of dataframe
dataset1.info()

# Importing Dataset2
dataset2 = pd.read_csv("/content/covid_grouped.csv")
dataset2.head()  # return first 5 rows of dataset2

# Returns tuple of shape (Rows, columns)
print(dataset2.shape)

# Returns size of dataframe
print(dataset2.size)

# Information about Dataset2
dataset2.info()  # return concise summary of dataframe

"""# Dataset cleaning"""

# Columns labels of a Dataset1
dataset1.columns

# Drop NewCases, NewDeaths, NewRecovered rows from dataset1

dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'],
              axis=1, inplace=True)

# Select random set of values from dataset1
dataset1.sample(5)

"""# Creating table using plotly express"""

# Import create_table Figure Factory

from plotly.figure_factory import create_table

colorscale = [[0, '#4d004c'], [.5, '#f2e5ff'], [1, '#ffffff']]
table = create_table(dataset1.head(15), colorscale=colorscale)
py.iplot(table)

"""# Bar graphs- Comparisons between COVID infected countries in terms of total cases, total deaths, total recovered & total tests"""

px.bar(dataset1.head(15), x = 'Country/Region',
       y = 'TotalCases',color = 'TotalCases',
       height = 500,hover_data = ['Country/Region', 'Continent'])

px.bar(dataset1.head(15), x = 'Country/Region', y = 'TotalCases',
       color = 'TotalDeaths', height = 500,
       hover_data = ['Country/Region', 'Continent'])

px.bar(dataset1.head(15), x = 'Country/Region', y = 'TotalCases',
       color = 'TotalDeaths', height = 500,
       hover_data = ['Country/Region', 'Continent'])

px.bar(dataset1.head(15), x = 'Country/Region', y = 'TotalCases',
       color = 'TotalTests', height = 500, hover_data = ['Country/Region', 'Continent'])

px.bar(dataset1.head(15), x = 'TotalTests', y = 'Country/Region',
       color = 'TotalTests',orientation ='h',  height = 500,
       hover_data = ['Country/Region', 'Continent'])

px.bar(dataset1.head(15), x = 'TotalTests', y = 'Continent',
       color = 'TotalTests',orientation ='h',  height = 500,
       hover_data = ['Country/Region', 'Continent'])

"""# Data Visualization through Bubble Charts-Continent Wise"""

px.scatter(dataset1, x='Continent',y='TotalCases',
           hover_data=['Country/Region', 'Continent'],
           color='TotalCases', size='TotalCases', size_max=80)

px.scatter(dataset1.head(57), x='Continent',y='TotalCases',
           hover_data=['Country/Region', 'Continent'],
           color='TotalCases', size='TotalCases', size_max=80, log_y=True)

px.scatter(dataset1.head(54), x='Continent',y='TotalTests',
           hover_data=['Country/Region', 'Continent'],
           color='TotalTests', size='TotalTests', size_max=80)

px.scatter(dataset1.head(50), x='Continent',y='TotalTests',
           hover_data=['Country/Region', 'Continent'],
           color='TotalTests', size='TotalTests', size_max=80, log_y=True)

px.scatter(dataset1.head(100), x='Country/Region', y='TotalCases',
           hover_data=['Country/Region', 'Continent'],
           color='TotalCases', size='TotalCases', size_max=80)

px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases',
           hover_data=['Country/Region', 'Continent'],
           color='Country/Region', size='TotalCases', size_max=80, log_y=True)

px.scatter(dataset1.head(10), x='Country/Region', y= 'TotalDeaths',
           hover_data=['Country/Region', 'Continent'],
           color='Country/Region', size= 'TotalDeaths', size_max=80)

px.scatter(dataset1.head(30), x='Country/Region', y= 'Tests/1M pop',
           hover_data=['Country/Region', 'Continent'],
           color='Country/Region', size= 'Tests/1M pop', size_max=80)

px.scatter(dataset1.head(30), x='Country/Region', y= 'Tests/1M pop',
           hover_data=['Country/Region', 'Continent'],
           color='Tests/1M pop', size= 'Tests/1M pop', size_max=80)

px.scatter(dataset1.head(30), x='TotalCases', y= 'TotalDeaths',
           hover_data=['Country/Region', 'Continent'],
           color='TotalDeaths', size= 'TotalDeaths', size_max=80)

px.scatter(dataset1.head(30), x='TotalCases', y= 'TotalDeaths',
           hover_data=['Country/Region', 'Continent'],
           color='TotalDeaths', size= 'TotalDeaths', size_max=80,
           log_x=True, log_y=True)

px.scatter(dataset1.head(30), x='TotalTests', y= 'TotalCases',
           hover_data=['Country/Region', 'Continent'],
           color='TotalTests', size= 'TotalTests', size_max=80,
           log_x=True, log_y=True)

"""# Advanced Data Visualization- Bar graphs for All top infected Countries


"""

px.bar(dataset2, x="Date", y="Confirmed", color="Confirmed",
       hover_data=["Confirmed", "Date", "Country/Region"], height=400)

px.bar(dataset2, x="Date", y="Confirmed", color="Confirmed",
       hover_data=["Confirmed", "Date", "Country/Region"],log_y=True, height=400)

px.bar(dataset2, x="Date", y="Deaths", color="Deaths",
       hover_data=["Confirmed", "Date", "Country/Region"],
       log_y=False, height=400)

df_US= dataset2.loc[dataset2["Country/Region"]=="US"]

px.bar(df_US, x="Date", y="Confirmed", color="Confirmed", height=400)

px.bar(df_US,x="Date", y="Recovered", color="Recovered", height=400)

"""# Visualization of Data in terms of Maps"""

px.choropleth(dataset2,
              locations="iso_alpha",
              color="Confirmed",
              hover_name="Country/Region",
              color_continuous_scale="Blues",
              animation_frame="Date")

px.choropleth(dataset2,
              locations='iso_alpha',
              color="Deaths",
              hover_name="Country/Region",
              color_continuous_scale="Viridis",
              animation_frame="Date" )

px.choropleth(dataset2,
              locations='iso_alpha',
              color="Recovered",
              hover_name="Country/Region",
              color_continuous_scale="RdYlGn",
              projection="natural earth",
              animation_frame="Date" )

px.bar(dataset2, x="WHO Region", y="Confirmed", color="WHO Region",
       animation_frame="Date", hover_name="Country/Region")

"""# Visualize text using Word Cloud"""

dataset3= pd.read_csv("/content/covid_grouped.csv")
dataset3.head()

dataset3.tail()

dataset3.groupby(["Confirmed"]).count()

