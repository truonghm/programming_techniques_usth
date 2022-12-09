import numpy as np

def get_data(file_name):
	with open(file_name,"rb") as f:
		arr = np.genfromtxt(f,delimiter=";",names=True,dtype=None, encoding='utf-8')
	return np.array([list(r) for r in arr])

if __name__ == "__main__":
	q1 = """
Create a population table from the data stored in the file "population.csv".
Display in the console the content of the population object.
	"""
	q2 = """
Display in the console the content of the objects population["sex"], population["weight"] and population["height"]
	"""

	q3 = """
Display in the console the content of the objects population[0], population[1].
	"""

	q4 = """
Display in the console the content of the objects population[1]["sex"], population[1]["weight"].
What do you conclude about the accessibility of the data ?
	"""
	print(q1)
	file_name = 'population.csv'
	population = get_data(file_name=file_name)
	print(population)
	print(q2)
	for n, col in enumerate(('sex', 'weight', 'height')):
		print(f'population["{col}"]: ', population[:,n,])

	print(q3)
	print(population[0])
	print(population[1])

	print(q4)
	print(population[1][0])
	print(population[1][1])
	print("The data  can be accessed by index and by column name.")