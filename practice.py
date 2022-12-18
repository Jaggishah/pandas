import pandas as pd
import re
df = pd.read_csv('pokemon_data.csv')

print(df.describe)
print(df.loc[df['Type 1'] == 'Grass'])
print(df.columns)
df['Total'] = df['HP'] + df['Attack']
print(df)
df.drop(columns=['Total'])
print(df.columns)
df.drop(columns=['Total'])
print(df["Total"])
print(df.sort_values(by='Speed',ascending=False))
# print(df.loc[df['Name'].str.contains('^pi', flags=re.I ,regex=True)])
print(df.loc[df['Name']=='Pikachu'])