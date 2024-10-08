#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# visualization
import seaborn as sns
# Importing the dataset
dataset =pd.read_csv('cleaned.csv')
# list of first five rows
dataset.head()


# In[35]:


# list of last five rows
dataset.tail()


# In[36]:


# shape
dataset.shape


# In[37]:


# It is also a good practice to know the columns and their corresponding data types
# along with finding whether they contain null values or not.
dataset.info()


# In[38]:


# to get a better understanding of the dataset,
# we can also see the statistical summary of the dataset.
dataset['rating'].describe()


# In[39]:


# We can also see the number of unique users and items in the dataset.
dataset.nunique()


# In[40]:


# check for missing values
dataset.isnull().sum()


# In[41]:


# what was the best year of sales
dataset.groupby('year')['amount'].count().plot(kind='bar',title='Year Wise Sales')


# In[42]:


# We can see that the year 2015 to 2018 had the best sales.
# what was the best month of sales
dataset_2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year']
<= 2018)]
dataset_2015_2018.groupby('month')['rating'].count().plot(kind='bar')


# In[43]:


# what brand sold the most in 2015 to 2018
dataset_2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year']
<= 2018)]
dataset_2015_2018.groupby('brand')['amount'].sum().sort_values(ascending
=False).head(10)\
.plot(kind='bar',title='Brand Wise Top 10 Sales 2015 to 2018',y='amount')


# In[44]:


# Create subplots with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
# Plot for 2016
top_selling_2016 = dataset[dataset['year'] ==2016].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
axs[0, 0].bar(top_selling_2016.index, top_selling_2016)
axs[0, 0].set_title('Top Selling Products in 2016')
axs[0, 0].tick_params(axis='x', rotation=45) # Rotate x-axis labels
# Plot for 2017
top_selling_2017 = dataset[dataset['year'] == 2017].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
axs[0, 1].bar(top_selling_2017.index, top_selling_2017)
axs[0, 1].set_title('Top Selling Products in 2017')
axs[0, 1].tick_params(axis='x', rotation=45) # Rotate x-axis labels
# Plot for 2018
top_selling_2018 = dataset[dataset['year'] ==2018].groupby('brand')['rating'].count().sort_values(ascending=False).head(10)
axs[1, 0].bar(top_selling_2018.index, top_selling_2018)
axs[1, 0].set_title('Top Selling Products in 2018')
axs[1, 0].tick_params(axis='x', rotation=45) # Rotate x-axis labels
# Hide the empty subplot
axs[1, 1].axis('off')
# Adjust layout for better appearance
plt.tight_layout()
# Show the plots
plt.show()


# In[45]:


# # What product by category sold the most between 2015 to 2018?
dataset2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year'] <= 2018)]
dataset2015_2018.groupby('category')['amount'].sum().sort_values(ascending=False).head(10).plot(kind='bar',
title='Top 10 Most Sold ProductCategory 2015 to 2018')


# In[46]:


# What product by brand name sold the least between 2015 to 2018?
dataset2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year'] <= 2018)]
dataset2015_2018.groupby('category')['amount'].sum().sort_values(ascending=True).head(10).plot(kind='bar',
title='10 Least Sold Product Brand 2015 to 2018')


# In[47]:


# What product by brand name sold the least between 2015 to 2018?
dataset2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year']<= 2018)]
dataset2015_2018.groupby('brand')['amount'].sum().sort_values(ascending=True).head(10).plot(kind='bar',
title='10 Least Sold Product Brand 2015 to 2018')


# In[48]:


# # the distribution of ratings
sns.countplot(x='rating', data=dataset)


# In[49]:


# What is the most rated brand name between 2015 to 2018?
dataset2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year']<= 2018)]
dataset2015_2018.groupby('brand')['rating'].mean().sort_values(ascending=False).head(10).plot(kind='bar',
title='10 most rating Brand 2015 to 2018')


# In[50]:


# category percentage sales
dataset.groupby('category')['amount'].sum().sort_values(ascending=False).head(5).plot(kind='pie', autopct='%1.1f%%',title='Top 5 category sales percentage')


# In[51]:

# brand wise sales percentage
dataset.groupby('brand')['rating'].count().sort_values(ascending=False).head(5).plot(kind='pie', autopct='%1.1f%%',title='Top 5 Brand wise sales percentage')

# In[52]:

# Gender wise customer distribution
gender_distribution = dataset['gender'].value_counts()
plt.pie(gender_distribution, labels=gender_distribution.index,
autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
plt.title('Gender wise customer Distribution')
plt.show()





