#!/usr/bin/env python
# coding: utf-8

# # What is a DataFrame?
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

# Q1. CREATE A SIMPLE PANDAS DATAFRAME

# In[1]:


import pandas as pd

data = {
        "calories": [420,380,390],
        "duration": [50,40,45]
}
#load data into  a dataframe object:
df = pd.DataFrame(data)
print(df)


# we can see in the above example pd.dataframe , we can see that D and F of dataframe after pd dot should be in capital, otherwise interpreter will not be recognizing what is dataframe like we saw in the series one.

# # Locate Row
# As you can see from the result above, the DataFrame is like a table with rows and columns.
# 
# Pandas use the loc attribute to return one or more specified row(s)

# Q2. RETURN ROW 0:

# In[2]:


#REFER TO THE ROW INDEX
print(df.loc[0])


# Note: This example returns a Pandas Series.

# Q3 RETURN ROW 0 AND 1:
# 

# In[5]:


print(df.loc[[0,1]])


# Note: When using [ ], the result is a Pandas DataFrame.

# # Named Indexes
# With the index argument, you can name your own indexes.

# Q4 Add a list of names to give each row a name:

# In[6]:


import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 


# BASICALLY BYDEFAULT INDEX IS 0,1,2 ETC BUT IF WE WANT TO CUSTOMIZE THEN INDEX ARGUMENT KA USE KARKE WE CAN EASILY USE.

# # Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).

# In[7]:


#RETURNING DAY2
print(df.loc["day2"])


# # Load Files Into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

# Q5. Load a comma separated file (CSV file) into a DataFrame:

# In[13]:


import pandas as pd

df = pd.read_csv("C:/Users/gguglani/Desktop/WAVE 2/UPLOAD CFD500 GTR AND GTP/customer number gentemp.csv")

print(df)


# in the above code we can see we have given the exact path to load and read our csv file. now there are three steps to load the csv file which are as belows:
# 1. pandas.read_csv(r"C:\Users\DeePak\Desktop\myac.csv")
# 2. pandas.read_csv("C:/Users/DeePak/Desktop/myac.csv")
# 3. pandas.read_csv("C:\\Users\\DeePak\\Desktop\\myac.csv")

# if we write in the below way then error ayega
# 
# import pandas as pd
# 
# df = pd.read_csv("C:\Users\gguglani\Desktop\WAVE 2\UPLOAD CFD500 GTR AND GTP\customer number gentemp.csv")
# 
# print(df)
# 
# or
# 
# df = pd.read_csv('C:\Users\gguglani\Desktop\WAVE 2\UPLOAD CFD500 GTR AND GTP\customer number gentemp.csv')

# # Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

# Q6 Create a simple Pandas Series from a dictionary:

# In[14]:


import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


# # Note: The keys of the dictionary become the labels.
# 
# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

# In[17]:


#Create a Series using only data from "day1" and "day2":

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

