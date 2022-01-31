import pandas as pd


x= {
    'Name' : ['Haider', 'Abdullha', 'Sufwan'],
    'Degree' : ["Engineer", "Doctor", 'Doctor']


}

xdf = pd.DataFrame(x)
xdf.to_csv('checkingerror.csv')

print(xdf.loc[(xdf['Name'] == 'Haider')])