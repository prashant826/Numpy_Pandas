#--------- Handle missing value in df ---------------

import numpy as np
import pandas as pd
from math import ceil

data = {
    'Name': ['John', 'Matt', np.nan, 'Cateline','John'],
    'math_Marks': [18, np.nan, 19, 15,18],
    'science_Marks': [1,20, 15, 12,np.nan]
}

df = pd.DataFrame(data)
df['Total'] = df.apply(lambda row: row['math_Marks'] + row['science_Marks'],axis=1)

# ------------------------------------------------------------
# ------------------ Method 1 dropNa -------------------------

# Not Recommended way of dealing with Null data.
# One should consult with client before using this operation.

# Step for calulating number of null value column-wise
#print(df.isna().sum())

# Deleting the rows based on column wise null values. 
df_cleaned = df.dropna(subset=['Name'])
#print(df_cleaned)

# Droping all the rows from entire dataset even in single column having a null value
df_cleaned = df.dropna()
#print(df_cleaned)

# for droping the value from existing dataframe we can set inplace argument = True
#df.dropna(inplace=True)

# ------------------------------------------------------------
# ------------------ Method 2 fillna -------------------------

# filling each row value with appropriate default values for null
# filling 'unspecified' for categorical data
# filling 0 for numerical null values.
df['Name'] = df['Name'].fillna('Unspecified')
#df['math_Marks'] = df['math_Marks'].fillna(0) # you can fill with mean strategy as well
#print(df)

# there are multiple method in fillna
# forward  fill (ffill) - fill the nan value with prev value.
# backward fill (bfill) - fill the nan value with next value.

df_forwad_fill = df.fillna(method='ffill')
df_backword_fill = df.fillna(method='bfill')
# Note - only drawback it will not work for boundary condition in science_marks column

df_cleaned_mean_strategy = df.fillna(df.mean())
print(df_cleaned_mean_strategy)