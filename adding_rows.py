import pandas as pd

newlistnm = ['Taha', 'Rafay', 'Mussab']
newlistci = ['Lahore', 'Multan', 'Lahore']
newlistmk = [100, 80, 90]

nm = ['Ahmad', 'Haider', 'Sufi']
ci = ['Islamabad', 'Sahiwal', 'Bahawalpur']
mk = [90, 70, 100]

nm = [*nm,*newlistnm]
ci = [*ci,*newlistci]
mk = [*mk,*newlistmk]

maindict = {
    'Name' : nm,
    'City' : ci,
    "Marks" : mk
}



maindataframe = pd.DataFrame(maindict)
maindataframe.to_csv("adding_rows.csv")




print(maindataframe)


print(maindataframe.loc[:,['Name']])

