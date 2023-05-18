import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# importing data
df = pd.read_csv('medical_examination.csv')
df.set_index ('id', inplace = True)

# adding 'overweight' column
df['overweight'] = df['weight'] / ((df['height'] / 100)**2)
df.loc[df.overweight <= 25, 'overweight'] = 0
df.loc[df.overweight > 25, 'overweight'] = 1
df.overweight = df.overweight.astype(int)

# normalizing data
df.loc[(df.gluc == 1), 'gluc'] = 0
df.loc[(df.gluc > 1), 'gluc'] = 1
df.loc[(df.cholesterol == 1), 'cholesterol'] = 0
df.loc[(df.cholesterol > 1), 'cholesterol'] = 1

def draw_cat_plot():
  # create, group, reformat the data
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
  df_cat = df_cat.groupby(['cardio', 'variable','value'])['value'].count().to_frame()
  df_cat.rename({'value': 'total'}, axis=1, inplace=True)
  df_cat.reset_index(inplace=True)

  # drawing categorical plot
  fig = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio', palette='Set2')

  fig.savefig('catplot.png')
  return fig

def draw_heat_map():
  # cleaning data
  df_heat = df[df['ap_lo'] <= df['ap_hi']]
  df_heat = df[df['height'] >= df['height'].quantile(0.025)]
  df_heat = df[df['height'] < df['height'].quantile(0.975)]
  df_heat = df[df['weight'] >= df['weight'].quantile(0.025)]
  df_heat = df[df['weight'] < df['weight'].quantile(0.975)]

  # calculating the correlation matrix
  corr = df_heat.corr().round(1)

  # generating a mask for the upper triangle
  mask = np.triu(np.ones_like(corr, dtype=bool))

  # drawing the heatmap
  fig, ax = plt.subplots(figsize=(10, 10))
  sns.heatmap(corr, mask=mask, annot=True, square=True)

  fig.savefig('heatmap.png')
  return fig