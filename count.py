import matplotlib.pyplot as plt
import pandas as pd

# Import text file which holds ImageStack's path
df = pd.read_csv('file.txt', header=None)
df.columns = ['paths']
# pandas string method extract takes a regex
df = df['paths'].str.extract('ASA_\w{3}_(.{6})(\d{4})(\d{2})(\d{2})')

# Columns 2=Year, 3=Month, 4=Day
df = df.ix[:, 1:4].astype(int)

# Set a name for columns
df.columns = ['year', 'month', 'day']

# Retrieve years from data for Legend and x axis
years = set(df.year)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Count occurrences per months and years
count = df.groupby(['year', 'month']).count()

# Plot based on Month
monthPlot = count.unstack(level=0).plot(kind='bar', stacked=True)
monthPlot.set_xticklabels(list(months[:]))
monthPlot.legend(years)

# Plot based on Year
yearPlot = count.unstack(level=1).plot(kind='bar', stacked=True)
yearPlot.legend(months)

plt.show()
