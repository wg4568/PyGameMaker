import pygame
pygame.M_1 = 323
pygame.M_2 = 324
pygame.M_3 = 325

def control_check():
	keys = list(pygame.key.get_pressed())
	mouse = pygame.mouse.get_pressed()
	keys.append(mouse[0])
	keys.append(mouse[1])
	keys.append(mouse[2])
	return keys

class Game(base.Base):
	def __init__(self):
		self.pygame = pygame
		pygame.init()

		self.title = "PyGameMaker"
		self.rate = 60
		self.size = [500, 500]
		self.background = (0, 0, 0)
		self.show_fps = True
		self.fps_color = (255, 255, 255)
		self.font = "freesansbold.ttf"

		self.running = False
		self.frame = 0
		self.clock = pygame.time.Clock()

	def _control(self):
		self.keys = control_check()
		self.mouse = pygame.mouse.get_pos()

		try: self.control(self.keys, self.mouse)
		except AttributeError: pass

	def _draw(self):
		self.screen.fill(self.background)

		try: self.draw()
		except AttributeError: pass

		if self.show_fps:
			self.draw_text("%iFPS" % self.fps, self.fps_color, (10, 10))

	def _logic(self):
		pass
		
		try: self.logic()
		except AttributeError: pass

	def load_textures(self):
		all_imgs = os.listdir(self.textures_file)
		for img in all_imgs:
			name = img.split(".")[0]
			path = os.path.join(self.textures_file, img)
			self.textures[name] = self.pygame.image.load(path)
			print "Loaded %s as %s" % (path, name)

	def draw_text(self, text, color, posn):
		text = self.font_obj.render(text, True, color)
		self.screen.blit(text, posn)

	def draw_rect(self, color, posn):
		self.pygame.draw.rect(self.screen, color, posn)

	def draw_ellipse(self, color, posn):
		self.pygame.draw.ellipse(self.screen, color, posn)

	def draw_image(self, image, posn):
		self.screen.blit(image, posn)

	def draw_texture(self, texture, posn, scale=None):
		img = self.textures[texture]
		if scale:
			if type(scale) not in [list, tuple]:
				scale = [scale] * 2
			img = self.pygame.transform.scale(img, scale)
		self.draw_image(img, posn)

	def set_font(self, path, size=12):
		self.font = path
		self.font_obj = self.pygame.font.Font(self.font, size)

	def stop(self):
		self.running = False

	def start(self):
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption(self.title)

		self.running = True
		self.fps = 0
		fps_time_counter = time.time()
		fps_counter = 0

		if self.textures_file:
			self.load_textures()

		try: self.on_start()
		except AttributeError: pass

		while self.running:
			fps_counter += 1
			if time.time()-fps_time_counter >= 0.5:
				fps_time_counter = time.time()
				self.fps = fps_counter*2
				fps_counter = 0

			self.frame += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					try: self.on_start()
					except AttributeError: pass
					self.running = False

			self._logic()
			self._control()
			self._draw()

			pygame.display.update()
			self.clock.tick(self.rate)