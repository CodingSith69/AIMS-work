import numpy as  np
import pandas as pd

data ={ 'Category':['melbourne_data','iowa_data','winchestor_data','New_York_data','Stanford']}

df= pd.DataFrame(data)

print("Original Dataframe: ")
print(df)

def One_Hot_Encoding(df,column):
    one_hot_df= pd.get_dummies(df[column],prefix=column)
    df= pd.concat([df,one_hot_df],axis=1)
    return df
df= One_Hot_Encoding(df,'Category')

print("\n DataFrame after One-Hot Encoding: ")
print(df)

    