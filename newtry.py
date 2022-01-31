import pandas as pd

y = ['Ahmad', 'Ali', 'haris', 'wasif', 'haider', 'mujahid']
z = [1,2,90,70,None,99]
x = {
    'name' : y,
    'marks' : z
}
xdf = pd.DataFrame(x)
print(xdf)
print(xdf.loc[(xdf['marks'] == 70)])

# print(xdf['marks'].isnull())


# print(xdf.loc[:, ['name']])
# xdf.dropna(inplace = True)
# print(xdf)