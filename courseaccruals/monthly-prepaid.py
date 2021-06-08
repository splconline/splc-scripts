#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path


# In[2]:


input_file = Path.cwd()/'course_income.csv'


# In[3]:


df = pd.read_csv(input_file)


# In[6]:


df.drop(['First Session', 'Day', 'Start', 'Sessions',
       'Tot-Stus', 'Concession-Stus', 'CM Fee', 'Operating Fee',
       'Concession Fee', 'Materials'], axis=1, inplace=True)


# In[8]:


df = df.sort_values('Code')


# In[10]:


df.to_csv('hurrah.csv',index=False)





