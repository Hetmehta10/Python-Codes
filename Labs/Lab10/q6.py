# Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable
# information.
import pandas as pd
import numpy as np

data = {'A': [1, np.nan, 3, np.nan, 5],
        'B': [np.nan, 'b', np.nan, 'd', np.nan],
        'C': [True, False, np.nan, np.nan, True]}
df = pd.DataFrame(data)

df_filled = df.fillna('Unknown')

print("DataFrame after replacing missing values:")
print(df_filled)