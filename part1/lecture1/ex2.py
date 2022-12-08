"""
Exercise 2: Prime number
1. Propose an algorithm that determines if a number n is prime, that is divisible only by 1 and itself.
2. Modify this algorithm so that it writes which are the first numbers among the first m integers.
"""

def check_prime(num:int) -> bool:
	if num == 0 or num == 1:
		return False

	for i in range(2, int(num/2)):
		if num%i == 0:
			return False

	return True 

def find_first_prime(nums:list):
	for n in nums:
		if isinstance(n, str):
			n = int(n)
		if check_prime(n):
			return n

	return

if __name__ == "__main__":
	ex = input("Select an exercise: 1 or 2: ")
	if ex == "1":
		num = int(input("Enter a positive integer: "))
		print(f"{num} is prime?: ", check_prime(num))
	if ex == "2":
		res = input("Enter a list of positive integers, separated by comma (1,2,3,4,5): ")
		nums = res.split(",")
		print("The first prime number in the list is: ", find_first_prime(nums))
	else:
		print("The number entered is invalid!")
