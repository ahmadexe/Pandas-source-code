import numpy as np 
import pandas as pd 
dict1 = {'name' : ['Ahmad', 'Sufi', 'Zoha', 'Fatima', 'Bhatti'],
'marks' : [97,96,95,94,93],
'city' : ['Sahiwal', 'Bahawalpur', 'Karachi', 'Colorado', 'Multan']
}

df = pd.DataFrame(dict1)
print(df)

#df.to_csv('family.csv')
print(df.head(2))
print(df.tail(2))
print(df.describe())

print(pd.read_csv('family.csv'))

