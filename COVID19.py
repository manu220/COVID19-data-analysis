# coding: utf-8
# Let's Import the modules 

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported')

# importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 

corona_dataset_csv = pd.read_csv("time_series_covid19_confirmed_global.csv")
corona_dataset_csv.head(10)

#Let's check the shape of the dataframe

corona_dataset_csv.shape

# Delete the useless columns

corona_dataset_csv.drop(['Lat','Long'],axis=1,inplace=True)
corona_dataset_csv.head(10)

# Aggregating the rows by the country

corona_dataset_aggregat=corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregat.shape
corona_dataset_aggregat.head(10)

#  Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

corona_dataset_aggregat.loc['China'].plot()
corona_dataset_aggregat.loc['India'].plot()
corona_dataset_aggregat.loc['Russia'].plot()
plt.legend()
corona_dataset_aggregat.loc['China']

# Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

corona_dataset_aggregat.loc['India'].diff().plot()
corona_dataset_aggregat.loc['Russia'].diff().plot()
plt.legend()
corona_dataset_aggregat.loc['India'].diff().max()

# caculating the first derivative of the curve

countries=list(corona_dataset_aggregat.index)

#find maxmimum infection rate for China


#find maximum infection rate for all of the countries. 

max_infection_rate=[]
for c in countries:
    max_infection_rate.append(corona_dataset_aggregat.loc[c].diff().max())
corona_dataset_aggregat['max infection rate']=max_infection_rate
corona_dataset_aggregat.head()

# create a new dataframe with only needed column 

corona_data=pd.DataFrame(corona_dataset_aggregat['max infection rate'])
corona_data.head()

# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# importing the dataset

world_happiness_report =pd.read_csv('worldwide_happiness_report.csv')
world_happiness_report.head()
world_happiness_report.shape

# let's drop the useless columns 

world_happiness_report.drop(['Overall rank','Score','Generosity','Perceptions of corruption'],axis=1, inplace=True)
world_happiness_report.head()

# changing the indices of the dataframe

x=world_happiness_report.groupby('Country or region').sum()
x.shape

# now let's join two dataset we have prepared  

# Corona Dataset :

corona_data.head()

#wolrd happiness report Dataset :

x.head()

data = x.join(corona_data).copy()
data.head()


# correlation matrix 

data.corr()

# Visualization of the results

# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

data.head()

# Plotting GDP vs maximum Infection rate

x=data['GDP per capita']
y=data['max infection rate']
sns.regplot(x,np.log(y))

# Plotting Social support vs maximum Infection rate

x=data['Social support']
sns.regplot(x,np.log(y))

# Plotting Healthy life expectancy vs maximum Infection rate

x=data['Healthy life expectancy']
sns.regplot(x,np.log(y))
