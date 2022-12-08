#!/usr/bin/env python
# coding: utf-8

# # Before we start, spin the wheel!

# In[1]:


# wh
import pandas as pd
df = pd.read_csv('student_pics.csv')
print(f"Winner is {df.sample(n=1).values[0][1]}")


# In[ ]:




