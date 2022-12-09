from pandas import Series,DataFrame
import numpy as np

df = DataFrame(np.random.randint(1,10,size=(2,3)),columns = ['one','two',"three"])
seats_column = Series([5,5])

df["Seats"] = seats_column
print(df)

