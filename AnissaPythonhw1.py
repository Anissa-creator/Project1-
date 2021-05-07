# Anissa Champion
#Pythonproject1_Covid 19 

##read in file
import matplotlib.pyplot as plt; plt.rcdefaults()
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df = pd.read_csv("cases.csv", error_bad_lines=False )


##print top of data
df.head()

##plt.bar(x=f['date'],
 
       ## height=f['positive'])
df.drop('County', inplace=True, axis=1)
print("The DataFrame object after deleting the column a")
print(df)
sum_row = {col: df[col].sum() for col in df}
# Turn the sums into a DataFrame with one row with an index of 'Total':
sum_df = pd.DataFrame(sum_row, index=["Total"])
# Now append the row:
df = df.append(sum_df)
print(df)
for row in df: 
    print(row, end = " ") 
df["sum"] = df.sum(axis=1)
print(df)
x = list_of_column_names
y = sum_df
plt.scatter(x,y)