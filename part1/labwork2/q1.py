"""
Load the data.zip file and extract it in your work folder.

With Pandas module, load the file "Viet Nam-2019.csv" and create a Dataframe.

Display the columns names, the number of row, the number of columns and the first lines of this Dataframe.

Indexes this Dataframe with the column "Age".
"""

import pandas as pd

def read_data(year:int):
	df = pd.read_csv(f"datas/Viet Nam-{year}.csv")
	return df
	
df = read_data(2019)
print("Column names:", df.columns)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("First line:")
print(df.head(1))
print("Index this dataframe with the column 'Age':")
df.set_index("Age", inplace=True)
print(df.head())