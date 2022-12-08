"""
Exercice 2: Robot class
We consider a class Robot representing a robot which can move in the space 2D. Each robot is characterized by a
name name (represented by a character string) a position pos (represented by a point in the space 2D).
1. Write the code of a class Robot allowing to represent the class Robot. By default, a robot is in position (0, 0) and
has the name ”John”.
2. Add in this class the accessors and mutators of the attributes name and pos.
"""

from ex1 import Point2D

class Robot:
	def __init__(self, name:str="John", pos:Point2D=Point2D()) -> None:
		self.__name = name
		self.__position = pos

	@property
	def name(self):
		return self.__name

	@property
	def position(self):
		return self.__position

	@name.setter
	def name(self, name):
		self.__name = name

	@position.setter
	def position(self, pos):
		self.__position = pos

	def __repr__(self) -> str:
		return f"Robot({self.__name}@({self.position.x},{self.position.y})"