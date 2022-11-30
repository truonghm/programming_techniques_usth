"""
Exercise 3: Display problems
Let N be an integer entered by the user such that N ≥ 0.
1. Write a program that displays N lines built like this (line numbers are also to be written) :
1 : *
2 : * *
3 : * * *
4 : * * **

2. Write a program that displays N lines constructed as follows :
   *
  ***
 *****
*******
"""

def display_stars_3a(num:int):
	for i in range(1, num+1):
		print(" " * (len(str(num)) - len(str(i))) + f"{i} : " + "* " * (i-1) + "*")

def display_stars_3b(num:int):
	for i in range(num):
		left_side = " " * (num - 1 - i) + "*" * i
		right_side = "*" * i + " " * (num - 1 - i)
		print(left_side + "*" + right_side)


if __name__ == "__main__":
	ex = input("Select an exercise: 1 or 2: ")
	if ex == "1":
		num = int(input("Enter an integer N such that N ≥ 0: "))
		display_stars_3a(num)
	if ex == "2":
		num = int(input("Enter an integer N such that N ≥ 0: "))
		display_stars_3b(num)
	else:
		print("The number entered is invalid!")