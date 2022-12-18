import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.groupby(['Type 1']).mean().sort_values(['Defense'],ascending=True))