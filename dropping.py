import pandas as pd
mydict = {
'name' : ['Ahmad', 'Haider', 'Sufi', 'Zoha'],
'pay' : [100000,90000,80000,70000],
'House no.' : ['1','2','3','4']

}






r = {'sports' : ['Karate', 'Football', 'Cricket','basketball']}
mydict.update(r)

mydf = pd.DataFrame(mydict)
print(mydf)

#xyz = mydf.drop("House no.", axis = 1)
#print(xyz)
