#!/usr/bin/python
# -*- coding: utf-8 -*-

#%%
import numpy as np 
import pandas as pd 

#%%
train = pd.read_csv("data/train.csv")
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

# %%
sample = train.iloc[0]
#%%
target_word = pd.DataFrame()
target_word = pd.concat([target_word,pd.Series( sample['text'].split())], ignore_index=True)



# %%
