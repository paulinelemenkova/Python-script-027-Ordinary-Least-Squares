#!/usr/bin/env python
# coding: utf-8
#
from __future__ import print_function
import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices
import os
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
y, X = dmatrices('profile ~ sedim_thick + igneous_volc + slope_angle', 
                 data=df, return_type='dataframe')
mod = sm.OLS(y, X)
res = mod.fit()
print(res.summary())
res.params
res.rsquared
sm.stats.linear_rainbow(res)
