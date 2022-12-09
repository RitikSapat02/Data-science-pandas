import pandas as pd
import numpy as np

my_dict = {
    'pokemon_height' : np.random.randint(20,100,5),
    'pokemon_weight' : np.random.randint(50,150,5),
    'pokemon_power'  : np.random.randint(150,280,5)
}

df = pd.DataFrame(my_dict)
print(df)

print(df.pokemon_height.mean())
print(df.sum())
print(df.pokemon_power.sum())
print(len(df))  
print(df.pokemon_power)
print(df["pokemon_power"])
print(df[df['pokemon_power']>250])

df["Name"] = ["Lambo","Audi","Porsch","Ferari","Aventado"]
print(df)
df["Name"] = df["Name"].str.lower()
print(df)