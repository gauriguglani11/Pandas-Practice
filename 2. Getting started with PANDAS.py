#!/usr/bin/env python
# coding: utf-8

# # Installation of Pandas

# If you have Python and PIP already installed on a system, then installation of Pandas is very easy.
# 
# Install it using this command:
# 
# C:\Users\Your Name>pip install pandas
# 
# If this command fails, then use a python distribution that already has Pandas installed like, Anaconda, Spyder etc.

# # Import Pandas
# 
# Once Pandas is installed, import it in your applications by adding the import keyword:
# 
# import pandas
# 
# Now Pandas is imported and ready to use.

# # Basic Example
# 

# In[2]:


import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


# Pandas DataFrame is two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
# 

# # Checking Pandas Version
# The version string is stored under __version__ attribute.

# In[3]:


import pandas as pd

print(pd.__version__)

