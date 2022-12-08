"""
Exercise 3: Calculate a histogram
1. create a data dictionary to store the number of occurrences of each character in a string ;
2. write a program that calculates the number of occurrences of a given character c in a string s.
3. modify this program by storing the number of occurrences of each character in a string s in the data dictionary
created in the first question.
"""

def create_dictionary():
	return {}

def count_char(char, string):
	return string.count(char)

def count_all_char(s):
	count_by_char = {}

	for char in s:
		if char in count_by_char:
			count_by_char[char] += 1
		else:
			count_by_char[char] = 1

	return count_by_char


if __name__ == "__main__":
	s = input("Enter a string:")
	print(count_all_char(s))