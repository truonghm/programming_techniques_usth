"""
Exercice 3: Board class
We represent a board with a 2D grid of points (grid) represented by a 2D list of points of N rows and M columns. It
also contains a list of objects of type Robot robots and an output exit of type Point2D.
1. Write the code of a Board class allowing to represent this class as well as its attributes. By default, a board has 8
rows and 8 columns, contains no robot and the output is at position (0, 0).
2. Add in this class the accessors and mutators of the attributes of the class Board.
3. Add a method which allows you to add a robot to the list of robots.
4. Add a method which allows to remove a robot of index i from the list of robots.
5. We consider that a cell of the board can be either a wall or an empty cell by means of a boolean (0 if the cell is a
wall ; 1 if the cell is free). Modify the attribute grid to represent this information.
6. We consider the method moveRobot allowing to move a robot from the list of robots to a position end. According
to the position of the considered robot and the presence of the walls, this method returns a boolean whose value
indicates if the robot can be moved to this position (1) or not (0), as well as the list of the traversed cells. Declare
and write the code of the function moveRobot.
"""

from typing import List
from collections import deque

class Point2D:
	def __init__(self, x = 0, y = 0) -> None:
		self._x = x
		self._y = y

	def _get_x(self):
		return self._x

	def _get_y(self):
		return self._y

	def _set_x(self, x):
		self._x = x

	def _set_x(self, y):
		self._y = y

	def __repr__(self) -> str:
		return f"Square({self.x},{self.y})"

	def is_valid(self) -> bool:
		return self.x >= 0 and self.y >= 0

class Robot:
	def __init__(self, name:str="John", pos:Point2D=Point2D()) -> None:
		self._name = name
		self._pos = pos

	def _get_name(self):
		return self._name

	def _get_position(self):
		return self._pos

	def _set_name(self, name):
		self._name = name

	def _set_position(self, pos):
		self._pos = pos