#!/usr/bin/env python
# coding: utf-8

# # Pandas series
# a pandas series is like a column in a table
# 
# It is a one-dimensional array holding data of any type

# Q1. CREATE A SIMPLE PANDAS SERIES FROM A LIST

# In[3]:


import pandas as pd

a = [1, 7, 2]

myvar = pd.series(a)

print(myvar)


# above we got error because we have written series as small s, always remember series mein it will be capital s

# In[4]:


import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)


# # Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# 
# This label can be used to access a specified value.

# Q2. RETURN THE FIRST VALUE OF THE SERIES:

# In[5]:


print(myvar[1])


# Q3. With the index argument, you can name your own labels.

# In[7]:


a = [4,5,6]

myvar1 = pd.Series(a, index = ["x","y","z"])

print(myvar1)


# When you have created labels, you can access an item by referring to the label.

# In[8]:


print(myvar1["y"])

