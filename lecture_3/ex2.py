"""
Exercice 2: Robot class
We consider a class Robot representing a robot which can move in the space 2D. Each robot is characterized by a
name name (represented by a character string) a position pos (represented by a point in the space 2D).
1. Write the code of a class Robot allowing to represent the class Robot. By default, a robot is in position (0, 0) and
has the name ”John”.
2. Add in this class the accessors and mutators of the attributes name and pos.
"""

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


