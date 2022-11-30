"""
Exercice 1: Point2D class
Consider a class Point2D representing a point in space 2D and characterized by two coordinates x and y.
1. Write the code of a class Point2D allowing to represent this class and its attributes with :
— a constructor by default initializes the values of x and y to 0 ;
— a constructor which initializes the values of x and y to values passed in parameter.
2. Add in this class the accessors (getters) and mutators (setters) of the attributes x and y
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