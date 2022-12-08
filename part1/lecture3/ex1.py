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
		self.__x = x
		self.__y = y

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	@x.setter
	def x(self, x):
		self.__x = x

	@y.setter
	def y(self, y):
		self.__y = y

	def is_valid(self) -> bool:
		return self.x >= 0 and self.y >= 0

	def __repr__(self) -> str:
		return f"Point2D({self.x},{self.y})"

	def __eq__(self, other):
		return self.__x == other.x and self.__y == other.y