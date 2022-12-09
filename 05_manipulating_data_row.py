
import pandas as pd
import numpy as np

numpy_array = np.random.randint(1,10,size=(3,2))
df = pd.DataFrame(numpy_array,index=[5,'forth',2],columns=['dog','cat'])
# print(df)

#----------------------df.drop()---------------------
# a = df.drop(2)
# print(a)
# print(df)

# # df.drop(2,inplace=True)
# print(df)

# # df.drop('forth',inplace=True)
# print(df)
# # df.drop([5,"forth"],inplace = True)
# # print(df.index)
# print(df)
# # print(df.index[0])
# # print(df.index[1])

# #------drop by index---------

# # df.drop(df.index[0],inplace = True)
# # df.drop(df.index[[0,2]],inplace = True)
# # print(df)

# print(df.dog > 3)

# print(df[df.dog > 2])
# print(df[df.dog == 5])

 
#------------------------add a row-----------------------------
# print(df.iloc[0])
# print(df.loc["forth"])

# df.loc[0] = [1,2]
# print()
# print(df)

#-------------------------------reset index ---------------------
df1 = pd.DataFrame(np.random.randint(1,30,size=(4,5)))
print(df1)
print("\n\n")
df1.drop(2,inplace=True)                #deleting a row with label 2
print(df1)                          #now labelling is breaked so use reset_index()
df1.reset_index(inplace=True,drop = True)
print("\n\n")
print(df1)