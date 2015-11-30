from matplotlib import cm
import matplotlib.pyplot as plt
import pandas as pd


def isPlot(fileName, colors=None, regex=None):
    # Import text file which holds ImageStack's path
    df = pd.read_csv(fileName, header=None)
    df.columns = ['paths']

    # pandas string method extract takes a regex
    if regex is not None:
        regPat = regex
    else:
        regPat = 'ASA_\w{3}_(.{6})(\d{4})(\d{2})(\d{2})'

    df = df['paths'].str.extract(regPat)

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
    # Colors: http://matplotlib.org/examples/color/colormaps_reference.html
    if colors is not None:
        cmap = colors
    else:
        cmap = cm.spectral
    monthPlot = count.unstack(level=0).plot(kind='bar', stacked=True,
                                            colormap=cmap)
    monthPlot.set_xticklabels(list(months[:]))
    monthPlot.legend(years)

    # Plot based on Year
    yearPlot = count.unstack(level=1).plot(kind='bar', stacked=True,
                                           colormap=cmap)
    yearPlot.legend(months)

    plt.show()
