"""
With the files "Viet Nam-2019.csv", "Viet Nam-2019.csv", create a graph wich show the variation of the population by age between 2019 and 2020 for each gender.

You must obtain the following result (the graph is visible in the folder graphs/variation_population_19_20.png in the moodle)
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(year:int):
	df = pd.read_csv(f"datas/Viet Nam-{year}.csv")
	df.set_index("Age", inplace=True)
	df.rename(columns={'M':f'M{year}', 'F':f'F{year}'}, inplace=True)
	return df

def plot():
	df = pd.concat([read_data(2019), read_data(2020)], axis=1)
	df['M'] = -df['M2019'] + df['M2020']
	df['F'] = -df['F2019'] + df['F2020']
	# print(df.head())
	df[['M','F']].plot(kind='bar', stacked=False, figsize=(10, 5))
	plt.title(f'Populatiton variation between 2019 and 2020')
	plt.xlabel("Age")
	plt.ylabel("Number of people")
	plt.grid()
	plt.xticks(rotation='horizontal')
	plt.show()

# plot(2019)
# plot(2020)

plot()