class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.path = {}
		self.insides = {}
		
	def go(self, direction):
		return self.path.get(direction, None)
		
	def add_paths(self, path):
		self.path.update(path)
		
	def grab_things(self, things):
		self.insides.update(things)
	
	def check_bag(self, things):
		self.insides.get(things, None)