#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv')

data.head()


# In[4]:


a = data[(data['fuel_type_code_pudl'] == 'coal') & (data.report_year == 1994)]['fuel_cost_per_unit_burned'].sum()
a


# In[5]:


b = data[(data['fuel_type_code_pudl'] == 'coal') & (data.report_year == 1998)]['fuel_cost_per_unit_burned'].sum()
b


# In[6]:


(b - a) / a


# In[7]:


data.report_year.dtype


# In[8]:


data.groupby('report_year')['fuel_cost_per_unit_delivered'].mean().idxmax()


# In[20]:


data.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].mean().idxmin()


# In[10]:


data['fuel_mmbtu_per_unit'].describe()


# In[ ]:





# In[11]:


data['fuel_qty_burned'].skew()


# In[12]:


data['fuel_qty_burned'].kurt()


# In[13]:


data.isnull().sum()


# In[14]:


data.info()


# In[15]:


data['fuel_unit'].isnull().sum()


# In[16]:


180/29522


# In[17]:


data['fuel_unit'].value_counts()


# In[18]:


data.corr()['fuel_cost_per_unit_burned'].sort_values()


# In[ ]:




