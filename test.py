import pandas as pd
from pandas.core.algorithms import duplicated


df = pd.read_csv('data.csv')

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
for x in df.index:
    if df.loc[x, 'Duration'] > df["Duration"].mean():
        df.loc[x, 'Duration'] = df["Duration"].mean()
    if df.loc[x, 'Calories'] > df["Calories"].mean():
        df.loc[x, 'Calories'] = df["Calories"].mean()
df['Duration'] = pd.to_numeric(df['Duration'])

print(df["Calories"].mean())
print(df["Duration"].mean())

print(df.corr())
