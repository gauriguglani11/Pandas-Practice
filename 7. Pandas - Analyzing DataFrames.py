#!/usr/bin/env python
# coding: utf-8

# # Pandas - Analyzing DataFrames
# 

# # Viewing the Data
# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# 
# The head() method returns the headers and a specified number of rows, starting from the top.

# GET A QUICK OVERVIEW BY PRINTING THE FIRST 10 ROWS OF THE DATAFRAME:

# In[1]:


import pandas as pd
df = pd.read_csv('C:/Users/gguglani/Desktop/WAVE 2/UPLOAD CFD500 GTR AND GTP/customer number gentemp.csv')

print(df.head(10))


# # Note: if the number of rows is not specified, the head() method will return the top 5 rows.
# 

# Q2. PRINT THE 1ST 5 ROWS OF THE DATAFRAME

# In[2]:


import pandas as pd
df = pd.read_csv('C:/Users/gguglani/Desktop/WAVE 2/UPLOAD CFD500 GTR AND GTP/customer number gentemp.csv')
print(df.head())


# BY DEFAULT 5 ROWS WILL BE PRINTED IF NO VALUE SPECIFIED

# There is also a tail() method for viewing the last rows of the dataframe
# 
# The tail() method returns the headers and a specified number of rows, starting from the bottom

# Q PRINT THE LAST 5 ROWS OF THE DATAFRAME:

# In[3]:


print(df.tail())


# # Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.

# In[4]:


print(df.info())


# # Result Explained
# 1. the result tells us there are 1418 entries and 2 columns
# 2. the name of the each column with datatype
# 3. The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 1418 Non-Null values in the "Customer" column.
# 
