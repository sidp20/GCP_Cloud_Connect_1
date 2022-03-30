#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install --upgrade google-cloud-storage


# In[8]:


pip install mysql-connector


# In[1]:


import numpy as np
import pandas as pd
import sqlite3
from google.cloud import storage
from datetime import datetime
import mysql.connector
import sys


# In[3]:


cnx = mysql.connector.connect(user='root', password='cool_proj@4321', host='34.135.223.177', database='scenario')

cursor = cnx.cursor()

query1 = ("select * from scenario")
cursor.execute(query1)
frame = pd.DataFrame(cursor.fetchall())


# In[4]:


frame.head()


# In[5]:


frame.columns = [['FY', 'deal_size', 'COLA', 'quality', 'inorganic', 'unrecog_revenue', 'reimburseables', 'cons_mix', 'out_mix', 'sc_serv_mix', 'int_serv_mix', 'tech_serv_mix', 'oper_serv_mix']]


# In[6]:


frame.head()


# In[ ]:




