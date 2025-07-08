#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using [Python] to model Salary based on Years of Experience.

# In[7]:


#Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error


# In[8]:


filename = "regression_data.csv"
x_col = "YearsExperience"
y_col = "Salary"


# In[9]:


df = pd.read_csv("regression_data.csv")


# In[10]:


#Describe the data
x = df[x_col].to_numpy()
y = df[y_col].to_numpy()


# In[11]:


# Create linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)


# In[15]:


# Data Plotting
plt.plot(x, y_pred, 'r-', label='Fitted Line')
plt.text(1.5, max(y) -1,
    f"y = {slope:.2f}x + {intercept:.2f}/n"
    f"r = {r_value:.2f}/nMSE = {mse:.2f}",
    fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regression")
plt.scatter(df[[x_col]], df[[y_col]], color='red')
plt.legend()
plt.savefig("regression_plot_python.png")
plt.show()                      


# In[22]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

