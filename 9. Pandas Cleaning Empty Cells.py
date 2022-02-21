#!/usr/bin/env python
# coding: utf-8

# # Pandas - Cleaning Empty Cells

# # Empty Cells
# Empty cells can potentially give you a wrong result when you analyze data.
# 
# 

# # Remove Rows
# One way to deal with empty cells is to remove rows that contain empty cells.
# 
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

# # Q1. Return a new Data Frame with no empty cells:

# In[1]:


import pandas as pd

df = pd.read_csv("C://Users//gguglani//Documents//DATA SCIENCE//PANDAS PRACTICE//data.csv")

new_df = df.dropna()

print(new_df.to_string())


# The dropna() function is used to remove missing values. Determine if rows or columns which contain missing values are removed. 0, or 'index' : Drop rows which contain missing values.

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# 
# If you want to change the original DataFrame, use the inplace = True argument:

# # Q2. Remove all rows with NULL values:

# In[2]:


import pandas as pd

df = pd.read_csv("C://Users//gguglani//Documents//DATA SCIENCE//PANDAS PRACTICE//data.csv")

df.dropna(inplace = True)

print(df.to_string())


# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.

# # Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# 
# This way you do not have to delete entire rows just because of some empty cells.
# 
# The fillna() method allows us to replace empty cells with a value:

# # Q3 Replace NULL values with the number 130:

# In[10]:


import pandas as pd

df = pd.read_csv("C://Users//gguglani//Documents//DATA SCIENCE//PANDAS PRACTICE//data.csv")

df.fillna(130, inplace = True)

print(df.to_string())


# Pandas DataFrame.to_string() function render a DataFrame to a console-friendly tabular output.

# # Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.
# 
# To only replace empty values for one column, specify the column name for the DataFrame:

# # Q4. Replace NULL values in the "Calories" columns with the number 130:

# In[13]:


import pandas as pd

df = pd.read_csv("C://Users//gguglani//Documents//DATA SCIENCE//PANDAS PRACTICE//data.csv")

df["Calories"].fillna(1000, inplace = True)

print(df.to_string())


# # Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# 
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# # Q5. Calculate the MEAN, and replace any empty values with it:

# In[19]:


import pandas as pd

df = pd.read_csv("C://Users//gguglani//Documents//DATA SCIENCE//PANDAS PRACTICE//data.csv")

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

#printing mean
print(x)

#printing data with the mean values added int he columns
print(df.to_string())


# Mean = the average value (the sum of all values divided by number of values).

# # Q6. Calculate the MEDIAN, and replace any empty values with it:

# In[20]:


import pandas as pd

df = pd.read_csv("C://Users//gguglani//Documents//DATA SCIENCE//PANDAS PRACTICE//data.csv")

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

#printing median
print(x)

#printing data with the mean values added int he columns
print(df.to_string())


# Median = the value in the middle, after you have sorted all values ascending.

# # Q7. Calculate the MODE, and replace any empty values with it:
# 

# In[22]:


import pandas as pd

df = pd.read_csv("C://Users//gguglani//Documents//DATA SCIENCE//PANDAS PRACTICE//data.csv")

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

#printing mode
print(x)

#printing data with the mean values added int he columns
print(df.to_string())


# Mode = the value that appears most frequently.
