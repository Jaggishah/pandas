import pandas as pd

df = pd. read_csv('pokemon_data.csv')
# print(df.head(4))
print(df.columns)
# print(df[['Name','HP']])

print(df.iloc[2,0])
print(df.iloc[0:2,0])