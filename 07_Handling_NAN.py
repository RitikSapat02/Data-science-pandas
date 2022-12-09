
from cmath import nan
import pandas as pd
import numpy as np

numpy_array = np.random.randint(1,10,size=(3,3))
df = pd.DataFrame(numpy_array,index=[5,'forth',2],columns=['dog','cat','animal'])

df["check"] = [np.NaN,4,np.NaN]
df["check2"] = [4,5,np.NaN]
print(df)

#----------dropna()---------
'''df.dropna(inplace = True)
print(df)'''

#----------fillna()--------
df["check"].fillna(df.check.mean(),inplace=True)
df.check2.fillna(df["check2"].mean(),inplace =True)
print(df)

