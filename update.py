import numpy as np
import pandas as pd

nam = ['Ahmad', 'Zoha', 'Haider', 'Saad']
marks = [90,80,70,60]
city = ['Islamabad', 'Karachi', 'Sahiwal', 'Karachi']

dictdb = {
'Names' : nam,
'Marks' : marks,
"City" : city
}
nam.append("Sufi")
marks.append(90)
city.append('Bwp')

df = pd.DataFrame(dictdb)

df.to_csv("trying.csv")