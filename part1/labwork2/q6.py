"""
With the files in the folder datas, create a graph wich show the variation of the population by age group between 1990 and 2020

You must obtain the following result (the graph is visible in the folder graphs/variation_age_group.png in the moodle):
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data():
	df_list = []
	for year in range(1990, 2023):
		df = pd.read_csv(f"sdatas/Viet Nam-{year}.csv")
		# df.set_index("Age", inplace=True)
		df['Year'] = year
		df[['age_lower','age_upper']] = df['Age'].str.split('-', n=2, expand=True)
		df['age_upper'] = np.where(
			df['age_upper'].isnull(), 
			'100', 
			df['age_upper']
			).astype(int)
		df['age_lower'] = np.where(
			df['age_lower']=='100+', 
			'100', 
			df['age_lower']
			).astype(int)

		conds = [
			(df['age_lower'] >= 0) & (df['age_upper'] <= 19),
			(df['age_lower'] >= 20) & (df['age_upper'] <= 39),
			(df['age_lower'] >= 40) & (df['age_upper'] <= 59),
			(df['age_lower'] >= 60) & (df['age_upper'] <= 79),
			(df['age_lower'] >= 80) & (df['age_upper'] <= 99),
			]
		choices = [
			'0-19',
			'20-39',
			'40-59',
			'60-79',
			'80-99'
		]
		
		df['age_group'] = np.select(conds, choices, default='100+')
		
		df_list.append(df)

	return pd.concat(df_list, axis=0)

def plot():
	df = read_data()
	df.to_csv('test.csv')
	df.sort_values(['Year','age_lower'], ascending=True, inplace=True)
	df['Total'] = df['M'] + df['F']
	df.drop(columns=['M','F', 'age_upper','age_lower','Age'], inplace=True)
	df_gr = df.groupby(['Year','age_group'])['Total'].sum().unstack()
	old_cols = df_gr.columns
	for col in [
			'0-19',
			'20-39',
			'40-59',
			'60-79',
			'80-99',
			'100+'
		]:
		df_gr[f"{col}_var"] = df_gr[col] - df_gr[col].shift(1)

	df_gr.drop(columns=old_cols, inplace=True)
	df_gr.columns = old_cols
	colors = ['steelblue','orange','green','red','purple','brown']
	df_gr.plot(kind='line', figsize=(15, 8), color=colors)
	plt.title(f'Variation of Vietnam population by age')
	plt.xlabel("Year")
	plt.xticks([i for i in range(min(df_gr.index), max(df_gr.index) + 1, 2)])
	plt.ylabel("Number of people")
	plt.grid()
	plt.show()

plot()