#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from patsy import dmatrices
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
y, X = dmatrices('profile ~ sedim_thick + igneous_volc + slope_angle',
                 data=df, return_type='dataframe'
                 )

# Fit and summary:
mod = sm.OLS(y, X)
res = mod.fit()
print(res.summary()
      )
