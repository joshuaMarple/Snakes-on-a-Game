class DungeonRoom():
	upperLeft 	= []
	lowerRight 	= []
	center 		= []

	def __init__(self, ux, uy, lx, ly):
		self.upperLeft = [ux, uy]
		self.lowerRight = [lx, ly]
		self.center = [ int((ux + lx) / 2), int((uy + ly) / 2)]

	def __str__(self):
		return "Upper Left: {} Lower Right: {} Center: {}".format(self.upperLeft, self.lowerRight, self.center)