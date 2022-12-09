import numpy as np
import pandas as pd

#try to create a dataframe 
user_data = {
    "MarksA" : np.random.randint(1,100,5),
    "MarksB" : np.random.randint(50,100,5),
    "MarksC" : np.random.randint(1,100,5)
}

print(user_data)

df = pd.DataFrame(user_data,dtype=int)
print(df)

print(df.head())                      #by default first observation

print(df.head(n = 4))

print(df.columns)
print(df.index)

#create a csv from dataframe
df.to_csv("marks.csv")

#create a dict  from dataframe
dic =  df.to_dict()
print(dic)

#Reading a csv file
my_data = pd.read_csv('marks.csv')
print(my_data)

my_data = my_data.drop(columns=['Unnamed: 0'])
print(my_data)

my_data.to_csv("marks2.csv",index = False)

#shape of dataframe
print(df.shape)

print(type(my_data))


#df.describe()
print(my_data.describe())

#df.tail()
print(df.tail())
print(df.tail(n = 3))


#accessing particular rows
print(df.iloc[3])


#accessing particular row and col
print(df.iloc[3,1])            #df.iloc[3][1]

idx = df.columns.get_loc('MarksB')
print(df.iloc[3,idx])

idx = [df.columns.get_loc('MarksB'),df.columns.get_loc("MarksC")]
print(df.iloc[3,idx])

print(df.iloc[:3,idx])


#sort the dataframe
print(my_data)

print(my_data.sort_values(by = ['MarksA'],ascending = True))
print(my_data.sort_values(by = ["MarksA"],ascending=False))

print(my_data.sort_values(by = ["MarksC","MarksA"],ascending= False))

#numpy array from dataframe
data_array = my_data.values
print(data_array)
print(type(data_array))


#Numpy array into dataframes
new_df = pd.DataFrame(data_array,dtype = 'int32',columns = ["Physics","Chemistry","Maths"])
print(new_df)
print(new_df["Physics"])
print(new_df.Physics)
print(new_df.isnull())
print(new_df.isnull().sum())