class DungeonRoom():
	upperLeft 	= []
	lowerRight 	= []
	center 		= []
	fill 		= False

	def __init__(self, ux, uy, lx, ly):
		self.upperLeft = [ux, uy]
		self.lowerRight = [lx, ly]
		self.center = [ int((ux + lx) / 2), int((uy + ly) / 2)]

	def __str__(self):
		return "Upper Left: {} Lower Right: {} Center: {}".format(self.upperLeft, self.lowerRight, self.center)

	def isIn(self, x, y):
		if self.upperLeft[0] <= x <= self.lowerRight[0]:
			if self.upperLeft[1] <= y <= self.lowerRight[1]: #since our coordinate system is flipped along the y axis
				return True
		return False