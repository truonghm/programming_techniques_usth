"""
With the files in the folder datas, create a graph wich show the variation of the population by age between 1990 and 2020

You must obtain the following result (the graph is visible in the folder graphs/variation_age.png in the moodle)
"""


import pandas as pd
import matplotlib.pyplot as plt

def read_data():
	df_list = []
	for year in range(1990, 2023):
		df = pd.read_csv(f"datas/Viet Nam-{year}.csv")
		# df.set_index("Age", inplace=True)
		df['Year'] = year
		df_list.append(df)

	return pd.concat(df_list, axis=0)

def plot():
	df = read_data()
	df['Total'] = df['M'] + df['F']
	df.drop(columns=['M','F'], inplace=True)
	df_gr = df.groupby(['Year','Age'])['Total'].sum().unstack()
	old_cols = df_gr.columns
	for col in df_gr.columns:
		df_gr[f"{col}_var"] = df_gr[col] - df_gr[col].shift(1)

	df_gr.drop(columns=old_cols, inplace=True)
	df_gr.columns = old_cols
	df_gr.plot(kind='line', figsize=(15, 8))
	plt.title(f'Variation of Vietnam population by age')
	plt.xlabel("Year")
	plt.xticks([i for i in range(min(df_gr.index), max(df_gr.index) + 1, 2)])
	plt.ylabel("Number of people")
	plt.grid()
	# plt.xticks(rotation='horizontal')
	plt.show()

plot()