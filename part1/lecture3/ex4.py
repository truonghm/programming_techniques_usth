"""
Exercice 4: Alice and Bob
This exercise is to test your classes.
1. Write a program that instantiates two robots named Alice and Bob and positioned as on the figure 1.
2. Complete this program in order to instantiate a tray of 11 rows and 11 columns with walls similar to the figure 1.
the robots Alice and Bob to the previous board in the list of robots in the board a method that allows you to
move Alice and Bob to the exit.
"""


import numpy as np
from ex3 import Point2D, Robot, Board

def main():
	alice = Robot("Alice", Point2D(9,1))
	bob = Robot("Bob", Point2D(5,5))

	def __build_grid():
		grid = np.ones((11,11), dtype=int)
		height, width = grid.shape
		for i in range(height):
			for j in range(width):
				if i == 0 and j == 1:
					pass
				elif i in (0, height-1) or j in (0, width-1):
					grid[i, j] = 0

		return grid

	exit = Point2D(0,1)
	board = Board(
		grid = __build_grid(),
		robots = [alice, bob],
		exit = exit
	)

	print(f"Original Board, contains {board.robots}, exit @ {board.exit}")
	print(board)
	print("\n---------------\n")
	_, alice_points = board.moveRobot('Alice')
	_, bob_points = board.moveRobot('Bob')
	print("The shortest path for Alice to get to the exit is:", alice_points)
	print("The shortest path for Bob to get to the exit is:", bob_points)
	print("\n---------------\n")
	print(board)

if __name__ == "__main__":
	main()