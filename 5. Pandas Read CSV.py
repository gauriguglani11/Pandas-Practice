#!/usr/bin/env python
# coding: utf-8

# # Read CSV Files
# A simple way to store big data sets is to use CSV files (comma separated files).
# 
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
# 
# In our examples we will be using a CSV file called 'customer number gentemp.csv'.

# In[1]:


# load the csv into dataframe
import pandas as pd

df = pd.read_csv('C:/Users/gguglani/Desktop/WAVE 2/UPLOAD CFD500 GTR AND GTP/customer number gentemp.csv')

print(df.to_string()) 


# use to_string() to print the entire DataFrame. so if we wanna see what is there in the file then with the help of to_string() method we can print it.

# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

#  Q1. print the dataframe without the to_string() method :

# In[2]:


import pandas as pd

df = pd.read_csv("C:/Users/gguglani/Desktop/WAVE 2/UPLOAD CFD500 GTR AND GTP/customer number gentemp.csv")
print(df)


# # max_rows
# The number of rows returned is defined in Pandas option settings.
# 
# You can check your system's maximum rows with the pd.options.display.max_rows statement.

# CHECK THE NUMBER OF MAXIMUM RETURNED ROWS:

# In[3]:


print(pd.options.display.max_rows) 


# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# 
# You can change the maximum rows number with the same statement.

# Q2 Increase the maximum number of rows to display the entire DataFrame:

# In[4]:


import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('C:/Users/gguglani/Desktop/WAVE 2/UPLOAD CFD500 GTR AND GTP/customer number gentemp.csv')

print(df) 

