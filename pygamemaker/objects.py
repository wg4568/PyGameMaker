class Object:
	def __init__(self, room):
		self.x = 0
		self.y = 0
		self.room = room
		self.sprites = {}
		self.current_sprite = None

		self.scale = 1

	def move_to(self, *args):
		if len(args) == 1: args = args[0]
		self.x, self.y = args

	def move_by(self, *args):
		if len(args) == 1: args = args[0]
		self.x += args[0]
		self.y += args[1]

	def set_scale(self, percent):
		self.scale = percent/100.0

	def change_scale(self, amount):
		self.scale += amount/100.0

	def add_sprite(self, name, sprite):
		self.sprites[name] = sprite

	def set_sprite(self, name):
		self.current_sprite = name

	def frame(self):
		try: self.logic()
		except AttributeError: pass

	def draw(self):
		self.sprites[self.current_sprite].draw(self.room, (self.x, self.y), scale=self.scale)
