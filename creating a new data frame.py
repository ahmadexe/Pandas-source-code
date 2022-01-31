import numpy as np 
import pandas as pd 


newdataframe = pd.DataFrame(np.random.rand(100,10), index = np.arange(1,101))

#print(newdataframe)
#print(newdataframe.dtypes)

#print(newdataframe.index)


#print(newdataframe.to_numpy())


newdataframe.loc[1,0] = 7138
print(newdataframe.head(2))
print(newdataframe.loc[1,1])