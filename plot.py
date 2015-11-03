import csv
import numpy as np
import matplotlib.pyplot as plt

# import csv file
with open('file.csv', 'rb') as f:
    reader = csv.reader(f)
    a = list(reader)

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

a = [[int(e) for e in d] for d in a]

years = set(d[0] for d in a)
nmonths = len(months)
minyear, maxyear = min(years), max(years)
nyears = maxyear - minyear + 1
monthly_counts = np.zeros((nyears, nmonths))

for year, month, _ in a:
    monthly_counts[year-minyear, month-1] += 1

fig, ax = plt.subplots()
ind = np.arange(nyears)
width = 0.45

# Random colors for the months
c = np.random.rand(nmonths, 3, 1)

p = []
for imonth in range(nmonths):
    p.append(ax.bar(ind, monthly_counts[:, imonth], width,
                    bottom=np.sum(monthly_counts[:, :imonth], axis=1),
                    color=c[imonth], alpha=0.8))

# Set x axis ticks and labels
ax.set_xticks(ind + width/2)
ax.set_xticklabels([str(minyear+i) for i in ind])

# Locate legend outside axes plot area
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend([pl[0] for pl in p], months, loc='center left',
          bbox_to_anchor=(1, 0.5))

plt.show()
