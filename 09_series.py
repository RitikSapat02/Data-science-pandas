import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# obj = Series([3,6,9,12])
# print(obj)
# print(obj.values)


ww2_cas = Series([8700000,4300000,3000000,21000000,400000], index=['USSR','Germany','China','Japan','USA'])
print(ww2_cas)

print(ww2_cas[ww2_cas > 4000000])

#convert series to dictionary
ww2_cas_dict = ww2_cas.to_dict()
print(ww2_cas_dict)


#read data from clipboard

frame = pd.read_clipboard()
print(frame)