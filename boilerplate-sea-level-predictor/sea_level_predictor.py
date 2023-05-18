import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # reading data
  df = pd.read_csv('epa-sea-level.csv')
  df.head()
    # creating scatter plot
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
  plt.figure(figsize=(15, 5))
  plt.scatter(x, y, alpha=0.5, color = 'grey', marker = 'X')
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')

    # creating first line of best fit
  years_ext = np.arange(1880, 2051, 1)
  slope, intercept, rvalue, pvalue, stderr = linregress(x, y)
  bf = [slope * i + intercept for i in years_ext]
  plt.plot(years_ext, bf, label = "Fitting Line 1880-2050", linewidth = 2, color = 'purple')

    # creating second line of best fit
  years_ext = np.arange(2000, 2051, 1)
  slope, intercept, rvalue, pvalue, stderr = linregress(x[x >= 2000], y[x >= 2000])
  bf = [slope * i + intercept for i in years_ext]
  plt.plot(years_ext, bf, label = "Fitting Line 2000-2050", linewidth = 2, color = 'navy')
      
    # save plot and return data for testing
  plt.savefig('sea_level_plot.png')
  return plt.gca()