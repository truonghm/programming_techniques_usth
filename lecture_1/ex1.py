"""
Exercise 1: Equation of second degree
We want to calculate the two roots, if they exist, of a second degree equation : ax2 + b.x + c = 0.
The program acquires the three coefficients A, B, C and provides: either the two roots, or the double root, or the unique
root if the equation is negative (i.e. if a=0), or the fact that the equation has no real root.
Write a program that computes and displays the solutions of this equation with A, B and C entered by the user.
"""
import math

def compute_roots(a:float, b:float, c:float) -> list:
	d = b**2 - 4*a*c

	if d > 0:
		x1 = (((-b) + math.sqrt(d))/(2*a))     
		x2 = (((-b) - math.sqrt(d))/(2*a))
		return [x1, x2]
	elif d == 0:
		return [(-b) / 2*a]
	else:
		return []

if __name__ == "__main__":
	input_str = input("Enter the coefficients A,B,C for the equation: Ax^2 + Bx + C = 0 (separated by comma): ")
	coefs = input_str.split(",")
	print("The roots of the equation are: ", compute_roots(int(coefs[0]), int(coefs[1]), int(coefs[2])))