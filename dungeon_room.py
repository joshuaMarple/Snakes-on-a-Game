import math
import sys

class DungeonRoom():
	upperLeft 	= []
	lowerRight 	= []
	center 		= []
	has_visited = False

	def __init__(self, ux, uy, lx, ly):
		self.upperLeft = [ux, uy]
		self.lowerRight = [lx, ly]
		self.center = [ int((ux + lx) / 2), int((uy + ly) / 2)]

	def __str__(self):
		return "Upper Left: {} Lower Right: {} Center: {}".format(self.upperLeft, self.lowerRight, self.center)

	def get_edges(self, rooms):
		edges = [RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge()]
		return_values = []
		for room in rooms:
			edge = RoomEdge(self, room)
			direction = edge.get_direction()
			if(direction == NO_DIRECTION):
				continue
			if(edge.get_distance() < edges[direction].get_distance()):
				edges[direction] = edge
		for edge in edges:
			if(edge.is_valid() == True):
				return_values.append(edge)
		return return_values


class RoomEdge():
	curr 	= None
	next	= None

	def __init__(self, fromRoom = None, toRoom = None):
		self.curr = fromRoom
		self.next = toRoom

	def get_distance(self):
		if(self.is_valid() == False):
			return sys.maxsize
		dx = self.curr.center[0] - self.next.center[0]
		dy = self.curr.center[1] - self.next.center[1]
		return math.sqrt(dx ** 2 + dy ** 2)

	def get_direction(self):
		if(self.is_valid() == False):
			return NO_DIRECTION
		dx = self.curr.center[0] - self.next.center[0]
		dy = self.curr.center[1] - self.next.center[1]
		if(dx == 0 and dy < 0):
			return NN
		elif(dx == 0 and dy > 0):
			return SS
		elif(dy == 0 and dx < 0):
			return WW
		elif(dy == 0 and dx > 0):
			return EE
		else:
			return NO_DIRECTION

	def is_valid(self):
		return self.curr != None and self.next != None

	def __str__(self):
		return "!! --- Edge --- !!\n\tcurr: {} \n\tnext: {}".format(self.curr, self.next)

NN 				= 0
EE 				= 1
SS 				= 2
WW 				= 3
NO_DIRECTION 	= -1
