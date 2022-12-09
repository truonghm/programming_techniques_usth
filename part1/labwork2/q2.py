"""
With the files "Viet Nam-2019.csv", "Viet Nam-2019.csv", create two graphs wich display the number of men and women by age.

You must obtain the following results (the graphs are visible in the folder graphs/Population_2019.png and graphs/Population_2020.png in the moodle)
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(year:int):
	df = pd.read_csv(f"datas/Viet Nam-{year}.csv")
	df.set_index("Age", inplace=True)
	return df

def plot(year):
	df = read_data(year)

	df.plot(kind='bar', stacked=False, figsize=(15, 5))
	plt.title(f'Population of Vietnam in {year}')
	plt.xlabel("Age")
	plt.ylabel("Number of people (in million)")
	plt.grid()
	plt.xticks(rotation='horizontal')
	plt.show()

plot(2019)
plot(2020)