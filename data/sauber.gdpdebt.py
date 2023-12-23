#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


url = "https://api.db.nomics.world/v22/series/AMECO/UDGG.csv?dimensions=%7B%22freq%22%3A%5B%22a%22%5D%2C%22unit%22%3A%5B%22percentage-of-gdp-at-current-prices-excessive-deficit-procedure%22%5D%2C%22geo%22%3A%5B%22deu%22%2C%22ita%22%2C%22fra%22%2C%22esp%22%5D%7D&limit=1000"

df_debt = pd.read_csv(url)


# In[3]:


df_debt


# In[6]:


df_debt.dtypes


# In[8]:


new_names = {df_debt.columns[0]: "Year",
            df_debt.columns[1]: "Germany",
            df_debt.columns[2]: "Spain",
            df_debt.columns[3]: "France",
            df_debt.columns[4]: "Italy"}
df_debt1 = df_debt.rename(columns = new_names)
df_debt1


# In[10]:


df_debt1.isna().sum()


# In[11]:


df_debt2 = df_debt1.dropna()
df_debt2


# In[12]:


df_debt3 = df_debt2.reset_index(drop=True)
df_debt3


# In[13]:


x = df_debt3["Year"]
countries = ["Germany", "Spain", "France", "Italy"]
for country in countries:
    plt.plot(x, df_debt3[country], label = country)
plt.legend()


# In[16]:


df_debt4 = pd.melt(
    df_debt3,
    id_vars = "Year",
    var_name = "Country",
    value_name = "Debt ratio"
)

df_debt4


# In[17]:


sns.lineplot(x = "Year", 
             y="Debt ratio", 
             hue = "Country", 
             data = df_debt4)


# In[18]:


df_debt5=pd.pivot(
    df_debt4,
    index = "Year",
    columns = "Country",
    values = "Debt ratio"
).reset_index()

df_debt5.head()


# In[ ]:





# In[ ]:




