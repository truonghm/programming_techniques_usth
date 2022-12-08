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

from typing import List, Optional
import numpy as np
from collections import deque

from ex2 import Robot, Point2D

class Board:
	def __init__(self, grid: Optional[List[List]] = [], robots: list = [], exit: Point2D = Point2D(0, 0)):
		if grid is None:
			grid = np.ones((8,8), dtype=int)
		else:
			grid = np.array(grid)
			if grid.ndim != 2:
				raise ValueError("The input array is not 2D")
			self.__grid = grid

		self.__robots = robots
		self.__exit = exit

	@property
	def grid(self):
		return self.__grid

	@grid.setter
	def grid(self, grid: List[List]):
		grid = np.array(grid)
		if grid.ndim != 2:
			raise ValueError("The input array is not 2D")
		self.__grid = grid
	
	@property
	def robots(self):
		return self.__robots

	@robots.setter
	def robots(self, robots):
		self.__robots = robots

	@property
	def exit(self):
		return self.__exit
	
	@exit.setter
	def exit(self, exit: Point2D = Point2D(0,0)):
		self.__exit = exit

	def add_robot(self, robot: Robot):
		self.__robots.append(robot)
		return self.__robots

	def remove_robot(self, index):
		self.__robots.pop(index)
		return self.__robots

	def update_robot_by_name(self, robot_name, **kwargs):
		idx, rb = self.select_robot_by_name(robot_name)
		if 'position' in kwargs:
			self.__robots[idx].position = kwargs['position']
		if 'name' in kwargs:
			self.__robots[idx].name = kwargs['name']

		return self.__robots[idx]
		
	def select_robot_by_name(self, robot_name):
		for idx, rb in enumerate(self.__robots):
			if rb.name == robot_name:
				return idx, rb

		raise ValueError("Robot does not exist.")

	def __repr__(self) -> str:
		new_grid = self.__grid.copy().astype(str)
		new_grid[(self.exit.x, self.exit.y)] = 'E'
		for rb in self.__robots:
			new_grid[(rb.position.x, rb.position.y)] = rb.name[0]

		return np.array2string(new_grid)

	def select(self, point:Point2D) -> bool:
		try:
			return self.__grid[point.x][point.y]
		except IndexError:
			return True
	
	def check_free_point(self, point:Point2D):
		if self.select(point) and point.is_valid:
			return True
		else:
			return False

	@staticmethod
	def get_neighbors(point:Point2D):
		neighbors = [
			Point2D(point.x - 1, point.y),
			Point2D(point.x + 1, point.y),
			Point2D(point.x, point.y - 1),
			Point2D(point.x, point.y + 1)
			]

		return neighbors
	
	def get_free_neighbors(self, point:Point2D) -> List[Point2D]:
		all_neighbor_pointss = self.get_neighbors(point)
		valid_neighbor_points = [sq for sq in all_neighbor_pointss if self.check_free_point(sq)]

		return valid_neighbor_points

	def get_reachable_points(self, point:Point2D) -> List[Point2D]:

		visited = [point]
		
		queue = deque()
		queue.append(point)
		reachable_points = []

		while len(queue) > 0:
			point = queue.popleft()
			reachable_points.append(point)

			for p in self.get_free_neighbors(point):
				if sq not in visited and self.check_free_point(p):
					visited.append(p)
					queue.append(p)

		return reachable_points

	def get_shortest_path(self, source:Point2D, destination:Point2D) -> List[Point2D]:

		visited = [source]
		
		queue = deque([[source]])

		while len(queue) > 0:
			path = queue.popleft()
			point = path[-1]

			if point == destination:
				return path

			for p in self.get_neighbors(point):
				if p not in visited and self.check_free_point(p):
					visited.append(p)
					queue.append(path + [p])

		return []

	def moveRobot(self, robot_name: str, source: Point2D = None, destination: Point2D = None) -> bool:

		idx, rb = self.select_robot_by_name(robot_name)
		if destination is None:
			destination = self.__exit
		if source is None:
			source = rb.position

		# print(destination, source)
	
		# reachable_points = self.get_reachable_points(source)
		shortest_path = self.get_shortest_path(source, destination)
		if len(shortest_path) != 0:
			self.__robots[idx].position = destination
			return True, shortest_path
		else:
			return False, []