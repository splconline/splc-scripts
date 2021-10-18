#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path


# In[2]:


input_file = Path.cwd()/'course_income.csv'


# In[3]:


df = pd.read_csv(input_file)


# In[4]:


df


# Lose unwanted columns then sort by Course Code

# In[5]:


df.drop(['Day', 'Start',
       'Tot-Stus', 'Concession-Stus', 'CM Fee',
       'Concession Fee', 'Materials'], axis=1, inplace=True)
df = df.sort_values('Code')


# In[6]:


df


# Make the '$1,200' strings numeric

# In[7]:


df['Total Income']=df['Total Income'].str.lstrip('$')
df['Operating Fee']=df['Operating Fee'].str.lstrip('$')
df['Total Income']=df['Total Income'].str.replace(',','')
df['Operating Fee']=df['Operating Fee'].str.replace(',','')
df['Total Income']=pd.to_numeric(df['Total Income'])
df['Operating Fee']=pd.to_numeric(df['Operating Fee'])


# While you're there, fix the dates too

# In[8]:


df['First Session'] = pd.to_datetime(df['First Session'])


# Add required blank columns, then reorder

# In[9]:


df['Category']=""
df['Facilitator']=""
df=df[['Category','Code','Course', 'Facilitator' , 'First Session','Sessions', 'Total Income','Operating Fee']]


# In[10]:


df


# Populate the category field

# In[11]:


df['Category'] = df['Code'].replace('(\d+)','',regex=True)


# In[12]:


df


# In[13]:


df=df.sort_values(['Category','Course'])


# In[14]:


# df.info()


# In[15]:


df.to_csv('hurrah.csv',index=False)


# In[ ]:




