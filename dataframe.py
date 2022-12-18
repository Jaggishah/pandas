import pandas as pd
data = {
    'Name':['jagggi','denowal','kalan'],
    'Address':['kalan','Garhshankar','asha'],
    'Age' : [21,31,43]
}
df = pd.DataFrame(data)
print(df['Name'])
df.to_excel('stuck.xlsx')