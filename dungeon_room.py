import math
import sys

class DungeonRoom():
	upperLeft 	= []
	lowerRight 	= []
	center 		= []
	has_visited = False
	fill 		= False

	def __init__(self, ux, uy, lx, ly):
		self.upperLeft = [ux, uy]
		self.lowerRight = [lx, ly]
		self.center = [ int((ux + lx) / 2), int((uy + ly) / 2)]

	def __str__(self):
		return "Upper Left: {} Lower Right: {} Center: {}".format(self.upperLeft, self.lowerRight, self.center)

	def get_edges(self, rooms):
		edges = [RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge()]
		filledges = [RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge(), RoomEdge()]
		return_values = []
		for room in rooms:
			edge = RoomEdge(self, room)
			direction = edge.get_direction()
			if(direction == NO_DIRECTION):
				continue
			if(edge.get_distance() < edges[direction].get_distance()):
				if(room.fill == True and edge.get_distance() < filledges[direction].get_distance() and edge.is_diagonal() == False):
					filledges[direction] = edge
				else:
					edges[direction] = edge


		if(filledges[NN].is_valid() == True and filledges[EE].is_valid() == True):
			edges[NE] = RoomEdge()
		if(filledges[SS].is_valid() == True and filledges[EE].is_valid() == True):
			edges[SE] = RoomEdge()
		if(filledges[NN].is_valid() == True and filledges[WW].is_valid() == True):
			edges[NW] = RoomEdge()
		if(filledges[SS].is_valid() == True and filledges[WW].is_valid() == True):
			edges[SW] = RoomEdge()

		for edge in edges:
			if(edge.is_valid() == True):
				return_values.append(edge)
		return return_values

	def isIn(self, x, y):
		if self.upperLeft[0] <= x <= self.lowerRight[0]:
			if self.upperLeft[1] <= y <= self.lowerRight[1]: #since our coordinate system is flipped along the y axis
				return True
		return False

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

		if(dy < 0):
			if(dx == 0):
				return NN
			elif(dx < 0):
				return NW
			elif(dx > 0):
				return NE

		if(dy > 0):
			if(dx == 0):
				return SS
			elif(dx < 0):
				return SW
			elif(dx > 0):
				return SE
		elif(dy == 0 and dx < 0):
			return WW
		elif(dy == 0 and dx > 0):
			return EE

		return NO_DIRECTION

	def is_diagonal(self):
		dirr = self.get_direction()
		if(dirr == NE or dirr == SE or dirr == SW or dirr == NW):
			return True
		return False

	def is_valid(self):
		return self.curr != None and self.next != None

	def __str__(self):
		return "!! --- Edge --- !!\n\tcurr: {} \n\tnext: {}".format(self.curr, self.next)

NN 				= 0
NE 				= 1
EE 				= 2
SE 				= 3
SS 				= 4
SW 				= 5
WW 				= 6
NW 				= 7
NO_DIRECTION 	= -1

