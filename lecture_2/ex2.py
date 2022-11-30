"""
Exercise 2: Browse a list
Write a program that creates a list of integers, then using successive runs of the list performs the following actions:
1. displays the list in columns;
2. counts the number of multiples of 3 present in the list ;
3. calculates the sum of all the even values of the list;
4. calculates the maximum and minimum of the elements of the list;
5. create a boolean true if the arithmetic mean of the values of the list is greater than or equal to 10; calculate the
product of all the values of the list included in the interval [50, 70] ;
6. displays the list in reverse (without creating a new list).
"""
from functools import reduce

def do_ex2():
	l = [5,8,13,21,34,55,89]
	print("The list L is:", l)
	print("-----")
	print("1. Displays the list in columns:")
	print("\n".join([str(i) for i in l]))
	print("-----")
	print("2. Number of multiples of 3:", len([i for i in l if i%3==0]))
	print("-----")
	print("3. Sum of all even values:", sum([i for i in l if i%2==0]))
	print("-----")
	print(f"4. Maximum value: {max(l)}, Minimum value: {min(l)}")
	print("-----")
	print("5: Is the arithmetic mean >= 10?:", sum(l)/len(l) >= 10)
	print("Product of all values in [50,70]:", reduce((lambda x, y: x * y), [i for i in l if i >= 50 and i <= 70]))
	print("-----")
	print("6. Display the list in reverse:", l[::-1])


if __name__ == "__main__":
	do_ex2()