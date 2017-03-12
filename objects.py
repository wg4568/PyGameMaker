import base

class Game(base.Base):
	def __init__(self):
		base.Base.__init__(self)

		self.title = "Object Testing"


game = Game()
game.start()