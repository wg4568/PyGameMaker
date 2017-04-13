import pygamemaker

#GAME CODE HERE

# red_box = sprites.Box((255, 0, 0), 10, 10)
# green_ellipse = sprites.Ellipse((0, 255, 0), 10, 10)
lava = pygamemaker.sprites.Image("resources/lava.png")
lava_irreg = pygamemaker.sprites.Image("resources/lava_irreg.png")

class Player(pygamemaker.objects.Object):
	def __init__(self, room):
		pygamemaker.objects.Object.__init__(self, room)

	def frame(self):
		# if self.x > 100:
		# 	self.set_sprite("lava")
		self.move_by(1, 1)

room = pygamemaker.rooms.Room()