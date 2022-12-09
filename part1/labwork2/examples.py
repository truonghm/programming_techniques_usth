import pandas as pd

#**************************************************************************
# LOAD AND EXPORT DATAS EXAMPLE
#**************************************************************************
# Load the datas contained in the file "Viet Nam-2020.csv" into a Dataframe
df1 = pd.read_csv("Viet Nam-2020.csv")
# Display the Dataframe
print(df1)
# Convert the Dataframe into a Serie
serie = df1.transpose()[0] 
#Confirm that the object is a Series
print (isinstance(serie, pd.Series))
# Export datas from Dataframe to an excel file with no index 
df1.to_excel("Viet Nam-2020.xlsx", index=False)
# Load the datas contained in the file "Viet Nam-2020.xlsx"
datas2 = pd.read_excel("Viet Nam-2020.xlsx")
# Create a DataFrame to represent datas
df2 = pd.DataFrame(datas2)
# Display df2
print(df2)

#**************************************************************************
# INSPECT DATAS EXAMPLE
#**************************************************************************
# Display the first line of the Dataframe df1
df1 = pd.read_csv("Viet Nam-2020.csv")
print(df1.head())
# Display the last line of the Dataframe df1
print(df1.tail())
# Display the number of columns and rows
print(df1.shape)
# Display a concise summary of the DataFrame
print(df1.info())
# Display statistical infos on the datas
print(df1.describe())

#**************************************************************************
# ACCESS TO THE ELEMENTS EXAMPLE
#**************************************************************************