"""
Exercise 6: Palindrome
Using the previous example, write a program that tests if a string (an array of characters) is a palindrome, i.e. that
the inverted
"""

def check_palindrome(l):
	return l == l[::-1]

if __name__ == "__main__":
	input_str = input("Enter a string: ")
	print("Is the string a palindrome?:", check_palindrome(input_str))

