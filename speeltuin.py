"""
Just for testing stuff.
"""
import pandas as pd
import numpy as np
import os

df = pd.read_csv('./reports/YouTube_video_Yoga PE - Mind | Yoga With Adriene.csv', index_col=0)
df = df.sort_values(by='likes', ascending=False)
print(df)
df.loc['Totals'] = df.sum()
df = pd.concat([df.loc[['Totals']], df[:-1]], axis=0)