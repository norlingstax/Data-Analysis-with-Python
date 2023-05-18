
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#reading data
df = pd.read_csv ('fcc-forum-pageviews.csv')

#cleaning data and parsing dates
filt = (df['value'] <= df['value'].quantile(0.025)) | (df['value'] >= df['value'].quantile(0.975))
df = df.drop(df[filt].index).reset_index(drop = True)
df['date'] = pd.to_datetime(df['date'])
df.set_index ('date', inplace = True)


def draw_line_plot():
  #drawing line plot
  fig = plt.figure(figsize=(10, 5))
  plt.plot(df.index, df['value'], color = 'grey')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.tight_layout()
  
  #save image and return figure
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  #copy and modify data for bar plot
  df_bar = df.copy()
  df_bar.reset_index(inplace=True)
  df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
  df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month
  df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

  #drawing bar plot
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  fig = df_bar.plot(kind='bar', figsize=(10,5))
  fig.legend(months, title='Months', prop={'size': 10})
  plt.xlabel("Years")
  plt.ylabel("Average Page Views")
  plt.grid(color='grey', linestyle=':', linewidth=2, axis='y', alpha=0.5)
  plt.tight_layout()
  fig = fig.figure
  
  #save image and return figure
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  #preparing data for box plots
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]
  df_box['num'] = df_box['date'].dt.month
  df_box = df_box.sort_values('num')

  #drawing box plots
  fig, axes = plt.subplots(ncols=2, figsize=(17,7))
  sns.boxplot(ax = axes[0], x = 'year', y = 'value', data = df_box).set(xlabel = 'Year', ylabel = 'Page Views', title = 'Year-wise Box Plot (Trend)')
  sns.boxplot(ax = axes[1], x = 'month', y = 'value', data = df_box ).set(xlabel = 'Month', ylabel = 'Page Views', title = 'Month-wise Box Plot (Seasonality)')
  plt.tight_layout()

  #save image and return figure
  fig.savefig('box_plot.png')
  return fig
