#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# d1: Last month Sales
d1 = {'Product ID': ["Shirt","Shoes","Hat","Tie","Socks","Necklace","Scarf"], "# Purchased": [46,33,84,65,99,64,21]}
# d2: This month Sales
d2 = {'Product ID': ["Gloves","Bracelet","Masks","Bow Tie","Glasses","Ear Muffs","Suits"], "# Purchased": [29,53,63,59,101,78,30]}


# In[3]:


df1 = pd.DataFrame(data=d1)
df2 = pd.DataFrame(data=d2)


# In[4]:


df1


# In[5]:


df2


# In[6]:


df1.merge(df2, how='outer')


# In[7]:


df1.merge(df2, how='inner')


# In[8]:


df1.merge(df2)


# In[9]:


pd.concat([df1, df2], axis=1)


# In[10]:


pd.concat([df1, df2])


# In[11]:


pd.concat([df1, df2], ignore_index=True)


# In[12]:


# Combined data from 2 departments in our store
combined = pd.concat([df1, df2], ignore_index=True)
combined


# In[13]:


# Market Competition
m1 = {'Product ID': ["Shirt","Masks","Hat","Tie","Glasses","Necklace","Sandles"], "# M_Purchased": 
      [36,37,77,67,83,59,45]}


# In[14]:


df3 = pd.DataFrame(data=m1)
display(df3)


# In[15]:


# Using inner... notice how 'inner' will only merger identitcal names (in this case that is "Product ID")
# inner is used to combine like terms IN BOTH tables

combined.merge(df3, how='inner')


# In[17]:


# pd. concat can take DataFrames as its argument, and is used to combine two DataFrames with same 
# columns or index, which can't be done with pd. concat since it will show the repeated column in the 
# DataFrame. Whereas join can be used to join two DataFrame s with different indices.

pd.concat([combined, df3], ignore_index=True, sort=True)


# In[40]:


# Using outer... notice how 'outer' will include all pieces of data and fill in with
# "NaN" for unavailable data types

combined.merge(df3, how='outer')


# In[16]:


# using inner is a way to clean your data (in a way) since you are not including the values that multiple data
# frames to



# concat is used to just add two sets together (columns don't have to match)
# merge matches up similar columns and shows more comparative data


# In[ ]:




