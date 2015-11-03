import pandas as pd

df = pd.read_csv('file.txt', header=None)
df.columns = ['paths']
# pandas string method extract takes a regex
s = df['paths'].str.extract('(\d{4})(\d{2})')

print s
