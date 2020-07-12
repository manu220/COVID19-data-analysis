#!/usr/bin/env python
# coding: utf-8

# # Welcome to Covid19 Data Analysis Notebook
# ------------------------------------------

# ### Let's Import the modules 

# In[ ]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ## Task 2 

# ### Task 2.1: importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 
# 

# In[32]:


corona_dataset_csv = pd.read_csv("time_series_covid19_confirmed_global.csv")
corona_dataset_csv.head(10)


# #### Let's check the shape of the dataframe

# In[33]:


corona_dataset_csv.shape


# ### Task 2.2: Delete the useless columns

# In[35]:


corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)


# In[37]:


corona_dataset_csv.head(10)


# ### Task 2.3: Aggregating the rows by the country

# In[43]:


corona_dataset_aggregat=corona_dataset_csv.groupby("Country/Region").sum()


# In[45]:


corona_dataset_aggregat.shape


# In[46]:


corona_dataset_aggregat.head(10)


# ### Task 2.4: Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

# In[58]:


corona_dataset_aggregat.loc['China'].plot()
corona_dataset_aggregat.loc['India'].plot()
corona_dataset_aggregat.loc['Russia'].plot()
plt.legend()


# In[60]:


corona_dataset_aggregat.loc['China']


# ### Task3: Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# In[65]:


corona_dataset_aggregat.loc['India'].diff().plot()
corona_dataset_aggregat.loc['Russia'].diff().plot()
plt.legend()


# In[66]:


corona_dataset_aggregat.loc['India'].diff().max()


# ### task 3.1: caculating the first derivative of the curve

# In[71]:


countries=list(corona_dataset_aggregat.index)
countries


# ### task 3.2: find maxmimum infection rate for China

# In[ ]:





# In[ ]:





# In[ ]:





# ### Task 3.3: find maximum infection rate for all of the countries. 

# In[73]:


max_infection_rate=[]
for c in countries:
    max_infection_rate.append(corona_dataset_aggregat.loc[c].diff().max())
max_infection_rate


# In[83]:


corona_dataset_aggregat['max infection rate']=max_infection_rate
corona_dataset_aggregat.head()


# ### Task 3.4: create a new dataframe with only needed column 

# In[81]:


corona_data=pd.DataFrame(corona_dataset_aggregat['max infection rate'])


# In[82]:


corona_data.head()


# ### Task4: 
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# ### Task 4.1 : importing the dataset

# In[91]:


world_happiness_report =pd.read_csv('worldwide_happiness_report.csv')
world_happiness_report.head()


# In[89]:


world_happiness_report.shape


# ### Task 4.2: let's drop the useless columns 

# In[93]:


world_happiness_report.drop(['Overall rank','Score','Generosity','Perceptions of corruption'],axis=1, inplace=True)


# In[94]:


world_happiness_report.head()


# ### Task 4.3: changing the indices of the dataframe

# In[97]:


x=world_happiness_report.groupby('Country or region').sum()
x.shape


# ### Task4.4: now let's join two dataset we have prepared  

# #### Corona Dataset :

# In[98]:


corona_data.head()


# #### wolrd happiness report Dataset :

# In[100]:


x.head()


# In[102]:


data = x.join(corona_data).copy()
data.head()


# ### Task 4.5: correlation matrix 

# In[103]:


data.corr()


# ### Task 5: Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[104]:


data.head()


# ### Task 5.1: Plotting GDP vs maximum Infection rate

# In[108]:


x=data['GDP per capita']
y=data['max infection rate']
sns.regplot(x,np.log(y))


# In[ ]:





# ### Task 5.2: Plotting Social support vs maximum Infection rate

# In[109]:


x=data['Social support']
sns.regplot(x,np.log(y))


# In[ ]:





# ### Task 5.3: Plotting Healthy life expectancy vs maximum Infection rate

# In[111]:


x=data['Healthy life expectancy']


# In[112]:


sns.regplot(x,np.log(y))


# ### Task 5.4: Plotting Freedom to make life choices vs maximum Infection rate

# In[113]:





# In[ ]:




