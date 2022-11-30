"""
Exercise 4: Recurring suite
Let the recurrent suite U be defined by :
{
	U_0 = 1,
	U_i+1 = {-U_i + 3 if U_i is divisible by 2; -3U_i + 1 else}
	}
with N ≥ 0.
Write a program that calculates and displays the terms of rank 0 to N with N entered by the user.
"""

def display_numbers(num):
	out = [1]

	if num == 0:
		return out

	for i in range(1, num+1):
		if i % 2 == 0:
			next_u = -1 * out[i-1] + 3
		else:
			next_u = -3 * out[i-1] + 1
		
		out.append(next_u)

	return out

if __name__ == "__main__":
	num = int(input("Enter an integer N such that N ≥ 0: "))
	print(display_numbers(num))