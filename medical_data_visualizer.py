import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pd.options.mode.copy_on_write = True

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = df['weight'] / pow(df['height'] / 100, 2)
df['overweight'] = 0
df.loc[bmi > 25, 'overweight'] = 1

# 3
df.loc[df['cholesterol'] <= 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] <= 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# 4
def draw_cat_plot():
   # 5
   global df
   df_cat = df.melt(
      ['cardio'],
      ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

   # 6
   df_cat = df_cat.groupby(
      ['cardio', 'variable', 'value'],
      as_index = False).value_counts()
   df_cat = df_cat.rename(columns = {'count': 'total'})
   
   # 7
   chart = sns.catplot(
      df_cat,
      col = 'cardio',
      hue = 'value',
      kind = 'bar',
      x = 'variable',
      y = 'total')

   # 8
   fig = chart.figure

   # 9
   fig.savefig('catplot.png')
   return fig

# 10
def draw_heat_map():
   # 11
   global df
   df_heat = df[(df['ap_lo'] < df['ap_hi']) &
      (df['height'] >= df['height'].quantile(0.025)) &
      (df['height'] <= df['height'].quantile(0.975)) &
      (df['weight'] >= df['weight'].quantile(0.025)) &
      (df['weight'] <= df['weight'].quantile(0.975))]

   # 12
   corr = df_heat.corr()

   # 13
   mask = np.triu(np.ones(corr.shape))

   # 14
   fig, ax = plt.subplots()

   # 15
   map = sns.heatmap(
      corr,
      annot = True,
      fmt = '.1f',
      mask = mask)

   # 16
   fig.savefig('heatmap.png')
   return fig
