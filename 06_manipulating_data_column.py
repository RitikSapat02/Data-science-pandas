
import pandas as pd
import numpy as np

numpy_array = np.random.randint(1,10,size=(3,3))
df = pd.DataFrame(numpy_array,index=[5,'forth',2],columns=['dog','cat','animal'])


#-------------deleting a column---------------------
#------drop()----
'''df.drop('dog',axis = 1,inplace = True)
print(df)'''

#------del keyword------
'''del df['dog']
print(df)'''

# df.columns = ['Dog',"Cat","Animal"]
# print(df)

#________________Adding a column------------------
# df["Horse"] = [4,5,6]
# print(df)


#--------------------calculator dtaframe--------------
df1 =pd.DataFrame(np.random.randint(1,10,size=(3,2)),columns=["A","B"])
df1["sum"] = df1["A"] + df1["B"] 
df1["sub"] = df1["A"] - df1["B"] 
df1["mul"] = df1["A"] * df1["B"]
df1["Div"] = df1["A"] / df1["B"]
df1["Class"] = "maths"
print(df1)
