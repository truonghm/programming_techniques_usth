"""
Exercise 1: To begin
Write a program that creates a list L of at least 5 integers then successively :
1. displays the value of L[4] ;
2. modifies the list by replacing L[1] by the number 17 and L[3] by the sum of the neighbouring elements L[2] and
L[4] ;
3. displays 12 times the value of the last term in the list.
"""

def do_ex1():
	l = [5,8,13,21,34,55,89]
	print("The list L is:", l)

	# displays the value of L[4]
	print("The value of L[4] is:", l[3])

	# modifies the list by replacing L[1] by the number 17 
	# and L[3] by the sum of the neighbouring elements L[2] andL[4]

	l[0] = 17
	l[2] = l[1] + l[3]
	print("The list L after being modified is:", l)
	# displays 12 times the value of the last term in the list.

	print("Display 12 times the value of the last term in the list:", (str(l[-1]) + ", ") * 11 + str(l[-1]))

if __name__ == "__main__":
	do_ex1()