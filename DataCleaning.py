#!/usr/bin/python
# -*- coding: utf-8 -*-

#%%
import numpy as np 
import pandas as pd 

#%%
train = pd.read_csv("train.csv")
train.head()

#%%
train.info()

# %%
train.describe()
# %%
train.describe(include=['O'])
# %%
train.isnull().sum()
# %%
