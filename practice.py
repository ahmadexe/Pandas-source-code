import pandas as pd

mydict = {

'Name' : ['Ahmad', 'Zuwanish', 'Waleed', 'Maleeka', 'Zaineb'],
'Marks' : [100, 95, 94, 93, 92],
'City' : ["Sahiwal", "Islamabad", "Okara", "Islamabad", "Murree"]



}

mydict = pd.DataFrame(mydict)
print(mydict)
mydict.to_csv('friends.csv')
mydict.to_csv('friendsf.csv', index=False) 
#HEADERS AND TAIL
print(mydict.head(2))
print(mydict.tail(2))


#NUMERICAL FUNcS

print(mydict.describe())

#HOW TO READ A CSV
read_family = pd.read_csv('family.csv')

# CHANGING VALUES
read_family['marks'][2] = 97
print(read_family)

read_family.to_csv('family.csv')


#Knowing Data Type
print(mydict.dtypes)
