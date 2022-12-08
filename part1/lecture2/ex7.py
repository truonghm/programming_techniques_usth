"""
Exercise 7: List 2D
A tray is a two-dimensional array that contains booleans. If tray[i][j] is True, there is a wall and if not, the cell
is free. The goal of the exercise is to write a function path taking a tray and the coordinates of two squares deb
and end and returns True if we can go from the square deb to the end square by moving horizontally and vertically. For example, if tray=[[True,False,False,False], [False,True,True,False]], path(tray,(1, 3),(1, 0)) will return False
and path(tray,(1, 3),(0, 1)) will return True.
1. Write a function neighborsCase that takes a tray and a square and returns the set of those horizontal or vertical
immediate neighbors that are on the tray and are free.
2. Write a function neighborsCases that takes a board and a set of cases and returns the set of all neighbors of those
cases.
3. Write a function reachable that takes a board and a square and returns the set of squares that can be reached
from that square by moving horizontally and vertically.
4. Write the function path.
"""

from typing import List
import numpy as np
from collections import deque

class Square:
	def __init__(self, x:int, y:int):
		self.x = x
		self.y = y

	def __repr__(self) -> str:
		return f"Square({self.x},{self.y})"

	def is_valid(self) -> bool:
		return self.x >= 0 and self.y >= 0


class Board:
	def __init__(self, array:List[List]):
		array = np.array(array)
		if array.ndim != 2:
			raise ValueError("The input array is not 2D.")

		self.array = array

	def __repr__(self) -> str:
		return np.array2string(self.array)

	def select(self, square:Square) -> bool:
		try:
			return self.array[square.x][square.y]
		except IndexError:
			return True
	
	def check_free_square(self, square:Square):
		if not self.select(square) and square.is_valid:
			return True
		else:
			return False

	def get_free_neighbors(self, square:Square) -> List[Square]:
		all_neighbor_squares = [
			Square(square.x - 1, square.y),
			Square(square.x + 1, square.y),
			Square(square.x, square.y - 1),
			Square(square.x, square.y + 1)
			]
		valid_neighbor_squares = [sq for sq in all_neighbor_squares if self.check_free_square(sq)]

		return valid_neighbor_squares

	def get_bulk_free_neighbors(self, squares:List[Square], recursive=False) -> List[Square]:
		valid_connected_squares = []
		for sq in squares:
			valid_connected_squares.extend(self.get_free_neighbors(sq))

		return valid_connected_squares

	def get_reachable_squares(self, square:Square) -> List[Square]:

		visited = np.zeros_like(self.array)
		visited[square.x][square.y] = 1
		
		queue = deque()
		queue.append(square)
		reachable_squares = []

		while len(queue) > 0:
			point = queue.popleft()
			reachable_squares.append(point)

			for sq in self.get_free_neighbors(point):
				if visited[sq.x][sq.y] == 0 and self.check_free_square(sq):
					visited[sq.x][sq.y] = 1
					queue.append(sq)

		return reachable_squares

	def check_path(self, source:Square, destination:Square) -> bool:
		if destination in self.get_reachable_squares(source):
			return True
		else:
			return False

def neighborsCase(board:list, square:tuple):
	return Board(board).get_free_neighbors(Square(*square))

def neighborsCases(board, squares):
	return Board(board).get_bulk_free_neighbors([Square(*sq) for sq in squares])

def reachable(board, square):
	return Board(board).get_reachable_squares(Square(*square))

def check_path(board, src, dest):
	return Board(board).check_path(Square(*src), Square(*dest))

if __name__ == "__main__":
	result = check_path([[True,False,False,False], [False,True,True,False]], (1,3), (0,1))
	print(result)