"""
Exercise 5: Dice thrower
The game consists of rolling two dice and trying to get two 6 out. When the user makes a 6 with one of his dice,
it is possible to keep this dice and to throw only the other dice. We suppose that the dice have issued the values D1 and D2.
1. Write the function rollDice which takes as parameters the value of the dice D1 and D2 and which returns the dice
to restart (or none)
2. Write a program that simulates a game loop: as long as the dice that come out do not match two 6, the computer
will throw dice again. This program must call the function rollDice.
"""

import random
# random.seed(420)

def rollDice(d1:int, d2:int) -> dict:
	if d1 == 6 and d2 == 6:
		return {"D1": False, "D2": False}
	elif d1 == 6:
		return {"D1": False, "D2": True}
	elif d2 == 6:
		return {"D1": True, "D2": False}
	else:
		return {"D1": True, "D2": True}

def rollDiceLoop():
	def reroll(dice:dict) -> dict:
		res = {"D1": 6, "D2": 6}
		if dice["D1"]:
			res["D1"] = random.randrange(1,7)
		if dice["D2"]:
			res["D2"] = random.randrange(1,7)

		return res
	
	dice = {"D1": True, "D2": True}
	counter = 1

	while dice["D1"] or dice["D2"]:
		dice_to_roll = [k for k,v in dice.items() if v]
		print(f"Turn {counter}, roll ", " and ".join(dice_to_roll), "!!!")
		res = reroll(dice)
		print("The results are: ", (", ").join([f"{d} - {res[d]}" for d in dice_to_roll]))

		dice = rollDice(res['D1'], res['D2'])
		counter += 1
		
	print("-----\nBoth dice get 6, stop!!!")


if __name__ == "__main__":
	rollDiceLoop()