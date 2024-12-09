#!/usr/bin/env python
# coding: utf-8

# # Car Dataset

# Here. The data of different cars is given with their specifications.

# This data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame.

# In[2]:


import pandas as pd


# In[3]:


car=pd.read_csv(r"C:\Users\Soami Computers\Downloads\archive (1).zip")


# In[ ]:


car


# In[6]:


car.head()


# In[7]:


car.shape


# # for data cleaning
# find all null value in the dataset if there is any null value in any column then fill it with the mean of that column

# In[8]:


car.isnull()


# In[9]:


car.isnull().sum()


# In[10]:


car['horsepower'].fillna(car['horsepower'].mean())


# In[11]:


car


# In[12]:


car.isnull().sum()


# Inplace command used to make a changes permanently

# In[14]:


car['horsepower'].fillna(car['horsepower'].mean(),inplace=True)


# In[15]:


car.isnull().sum()


# In[16]:


car


# In[17]:


car.head(2)


# based on value count

# In[18]:


car['name'].value_counts()


# # filtering
# show all the records where origin is asia or europe

# In[19]:


car[car['origin'].isin(['asia','europe'])]


# # removing unwanted records
# removing  all the records (rows) where weight is above 3000

# In[20]:


car[~(car['weight']>3000)]


# # applying function on a column
# increase all the values of model_year column by 3

# In[21]:


car['model_year'] = car['model_year'].apply(lambda x:x+3)


# In[22]:


car

