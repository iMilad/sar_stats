import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import text file which holds ImageStack's path
df = pd.read_csv('file.txt', header=None)
df.columns = ['paths']
# pandas string method extract takes a regex
df = df['paths'].str.extract('ASA_\w{3}_(.{6})(\d{4})(\d{2})(\d{2})')

# Columns 2=Year, 3=Month, 4=Day
df = df.ix[:, 1:4].astype(int)

df.columns = ['year', 'month', 'day']

count = df.groupby(['year', 'month']).count()
count.columns = ['count']

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

nmonths = len(months)
fig, ax = plt.subplots()
ind = np.arange(nmonths)
width = 0.45

nyears = len(count.index.levels[0])
p = []
for year in count.index.levels[0]:
    df_empty = pd.DataFrame({'months': ind})
    monthly_sum = df_empty.join(count.ix[year, :].groupby(level=0).sum())['count'].values
    counts_until = df_empty.join(count.ix[:year, :].groupby(level=1).sum())['count'].values
    p.append(ax.bar(ind, monthly_sum, width,
                    bottom=counts_until, alpha=0.8))

# Set x axis ticks and labels
ax.set_xticks(ind + width/2)
ax.set_xticklabels([months[i] for i in ind])

# Locate legend outside axes plot area
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend([pl[0] for pl in p], count.index.levels[0], loc='center left',
          bbox_to_anchor=(1, 0.5))

plt.show()
