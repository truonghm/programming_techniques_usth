"""
Exercise 4: Exchange of values
Write a program that exchanges the values of the first and last cells of any non-empty list.
"""

def exchange_first_last_value(l):
	if len(l) == 0:
		return l
	
	tmp = l[-1]
	l[-1] = l[0]
	l[0] = tmp

	return l

if __name__ == "__main__":
	input_str = input("Enter a non-empty list, separated by comma (square brackets not needed): ")
	l = input_str.split(",")

	print(exchange_first_last_value(l))