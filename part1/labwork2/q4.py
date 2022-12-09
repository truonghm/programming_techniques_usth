"""
With the files in the folder datas, create a graph wich show the variation of the population between 1990 and 2020 for each gender.

You must obtain the following result (the graph is visible in the folder graphs/variation_sex.png in the moodle):


In the previous graph, the years are not sorted. Change the previous graph in order to display the years in a sorted way.

You must obtain the following result (the graph is visible in the folder graphs/variation2_sex.png in the moodle):
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

def plot_varition_sex():
	df = read_data()
	df['Total'] = df['M'] + df['F']
	df_gr = df.groupby('Year').agg({'F':'sum','M':'sum','Total':'sum'})
	for col in df_gr.columns:
		df_gr[f"{col}_var"] = df_gr[col] - df_gr[col].shift(1)

	df_gr.drop(columns=['Total','M','F'], inplace=True)
	df_gr.columns = ['Women','Men','Total']
	# plt.figure(figsize=(15,5))
	df_gr.plot(kind='line', figsize=(15, 5))
	plt.title(f'Variation of Vietnam population')
	plt.xlabel("Year")
	plt.xticks([i for i in range(min(df_gr.index), max(df_gr.index) + 1, 2)])
	plt.ylabel("Number of people")
	plt.grid()
	# plt.xticks(rotation='horizontal')
	plt.show()

def plot_varition2_sex():
	df = read_data()
	df['Total'] = df['M'] + df['F']
	df_gr = df.groupby('Year').agg({'F':'sum','M':'sum','Total':'sum'})
	for col in df_gr.columns:
		df_gr[f"{col}_var"] = df_gr[col] - df_gr[col].shift(1)

	df_gr.drop(columns=['Total','M','F'], inplace=True)
	df_gr.columns = ['Women','Men','Total']
	df_gr.sort_index(ascending=True, inplace=True)
	# plt.figure(figsize=(15,5))
	df_gr.plot(kind='line', figsize=(15, 5))
	plt.title(f'Variation of Vietnam population')
	plt.xlabel("Year")
	plt.xticks([i for i in range(min(df_gr.index), max(df_gr.index) + 1, 2)])
	plt.ylabel("Number of people")
	plt.grid()
	# plt.xticks(rotation='horizontal')
	plt.show()

plot_varition_sex()
plot_varition2_sex()