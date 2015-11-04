import pandas as pd

df = pd.read_csv('file.txt', header=None)
df.columns = ['paths']
# pandas string method extract takes a regex
df = df['paths'].str.extract('ASA_\w{3}_(.{6})(\d{4})(\d{2})(\d{2})')

# Columns 2,3,4
df = df.ix[:, 1:4]

# Save it as a csv file
df.to_csv('out.csv', sep=',', header=False, index=False)
