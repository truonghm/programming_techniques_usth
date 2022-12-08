"""
Exercise 5: List symmetry
Write a program that displays whether a list is symmetric (list identical to the list in reverse).
"""

def check_symmetric(l):
	return l == l[::-1]

if __name__ == "__main__":
	input_str = input("Enter a non-empty list, separated by comma (square brackets not needed): ")
	l = input_str.split(",")
	print("Is the list symmetric?:", check_symmetric(l))

