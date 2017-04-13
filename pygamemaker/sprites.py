import pygame

class Box:
	def __init__(self, color, width, height):
		self.width = width
		self.height = height
		self.color = color

	def draw(self, room, posn, scale=1):
		room.draw_rect(self.color, list(posn) + [self.width*scale, self.height*scale])

class Ellipse:
	def __init__(self, color, width, height):
		self.width = width
		self.height = height
		self.color = color

	def draw(self, room, posn, scale=1):
		room.draw_ellipse(self.color, list(posn) + [self.width*scale, self.height*scale])

class Image:
	def __init__(self, path):
		self.path = path
		self.surf = pygame.image.load(self.path)
		self.size = self.surf.get_rect().size

	def draw(self, room, posn, scale=1):
		size = map(lambda x: int(x*scale), self.size)
		img = pygame.transform.scale(self.surf, size)
		room.draw_image(img, posn)