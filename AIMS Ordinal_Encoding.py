import pandas as pd
import numpy as np

#Taking the example of a customer review system we an ordinal encode the following.

data = {'Category': ['Very Satisfied', 'Satisfied', 'Average Experience', 'Poor', 'Dissatisfied', 'Very Dissatisfied']}

df = pd.DataFrame(data)

print("The Original DataFrame is :")
print(df)#printing the original Dataframe.


ordinal_mapping = {'Very Dissatisfied': 0, 'Dissatisfied': 1, 'Poor': 2, 'Average Experience': 3, 'Satisfied': 4,'Very Satisfied':5}

df['Category_Ordinal'] = df['Category'].map(ordinal_mapping)

print("\n The resultant DataFrame after Ordinal Encoding is :")
print(df)