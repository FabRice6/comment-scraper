"""
Just for testing stuff.
"""
import pandas as pd
import numpy as np
import json
import os

# df = pd.read_excel('./reports/YouTube_video_Yoga PE - Mind | Yoga With Adriene.xlsx', index_col=0)

with open('data/comments_WomensHealthMag_top15.json', 'r') as fp:
    comments_and_likes = json.load(fp)

print(len(comments_and_likes['comments']['text']))