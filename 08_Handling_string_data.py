
from cmath import nan
import pandas as pd
import numpy as np

numpy_array = np.random.randint(1,10,size=(6,3))
df = pd.DataFrame(numpy_array,columns=['dog','cat','animal'])

df["Gender"] = ["male","male","female","female","female","male"]
print(df)
def change_into_number(m):
    if(m == "male"):
        return 1
    else:
        return 0

df['gender'] = df.Gender.apply(change_into_number)
df.drop("Gender",inplace=True,axis = 1)
print(df)