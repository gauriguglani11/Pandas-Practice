#!/usr/bin/env python
# coding: utf-8

#    # Pandas - Removing Duplicates

# # Discovering Duplicates
# Duplicate rows are rows that have been registered more than one time.
# By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
# 
# To discover duplicates, we can use the duplicated() method.
# 
# The duplicated() method returns a Boolean values for each row:

# # Q1. Returns True for every row that is a duplicate, othwerwise False:

# In[1]:


import pandas as pd

df = pd.read_csv("C://Users//gguglani//Documents//DATA SCIENCE//PANDAS PRACTICE//data.csv")
print(df.duplicated())
print(df.to_string())


# # Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.

# # Q2. Remove all duplicates:

# In[2]:


import pandas as pd

df = pd.read_csv("C://Users//gguglani//Documents//DATA SCIENCE//PANDAS PRACTICE//data.csv")

df.drop_duplicates(inplace = True)
print(df.to_string())


# #Notice that row 12 has been removed from the result

# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.
