import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1,2,3,4,5],[6,7,8,9,20]]),
index = ["one",'Two'],
columns = ['first','second','third','forth','fifth'])

df_copy = df.copy()
print(df)

print(df.dtypes)
print(df.columns)
print(df.index)
print(df["first"])
print(df.second)

print(df.isnull())
print(df.isnull().sum())