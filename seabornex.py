# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:01:53 2017

@author: rbabu
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
diabetes = pd.read_csv("C:\\Users\\rbabu\\Documents\\datascience\\diabetes.csv")
print(diabetes.isnull().sum())
print(diabetes.head())
sns.countplot(x='Outcome',data=diabetes)
plt.show()
