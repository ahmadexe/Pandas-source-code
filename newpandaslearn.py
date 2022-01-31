import pandas as pd


gn = ['valorant', 'cod', 'gta5']
gt = ['2020', '2012', '2016']


maindict = {
    'name' : gn,
    'Release Date' : gt
}


maindf = pd.DataFrame(maindict)                      #You can pass a complete data frame to to_csv function or a changed value
maindf.to_csv('trying_new_stuff.csv', index = False)


# print(maindf)
# print(maindf.describe())
# main_read_func = pd.read_csv('trying_new_stuff.csv')
# print(main_read_func)

# print(main_read_func['name'][0])

# main_read_func['name'][0] = 'san andreas'
# main_read_func.to_csv('trying_new_stuff.csv')                 #You can pass a changed value to to_csv function
# print(pd.read_csv('trying_new_stuff.csv'))



print(maindf.columns)


