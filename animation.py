
import turtle


wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("white")

# Register shapes
wn.register_shape("LinkR1.gif")
wn.register_shape("LinkR2.gif")
wn.register_shape("LinkR3.gif")
wn.register_shape("LinkR4.gif")
wn.register_shape("LinkR5.gif")
wn.register_shape("LinkR6.gif")
wn.register_shape("LinkR7.gif")
wn.register_shape("LinkR8.gif")
wn.register_shape("LinkU1.gif")
wn.register_shape("LinkU2.gif")
wn.register_shape("LinkU3.gif")
wn.register_shape("LinkU4.gif")
wn.register_shape("LinkU5.gif")
wn.register_shape("LinkU6.gif")
wn.register_shape("LinkU7.gif")
wn.register_shape("LinkU8.gif")

class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.shape("LinkR1.gif")
		#self.color("green")
		self.frame = 0
		self.direction = "stop"
		self.framesR = ["LinkR1.gif", "LinkR2.gif", "LinkR3.gif", "LinkR4.gif", \
						"LinkR5.gif", "LinkR6.gif", "LinkR7.gif", "LinkR8.gif"]
		self.framesU = ["LinkU1.gif", "LinkU2.gif", "LinkU3.gif", "LinkU4.gif", \
						"LinkU5.gif", "LinkU6.gif", "LinkU7.gif", "LinkU8.gif"]

	def jogRight(self):
		self.frame += 1
		if self.frame >= len(self.framesR):
			self.frame = 0
		self.shape(self.framesR[self.frame])
'''
    NEED HELP HERE***********************
    If I use wn.ontimer, the animation does not stop. This is not what I want.
    I want the animation to play only when the right arrow key is held. This currently works, but the animation runs too fast.
    How can I get the same type of delay achieved in the below code, but with the animation only playing when the arrow key
    is held down?
'''
		# Set timer
		#wn.ontimer(self.jogRight, 100)



	def jogUp(self):
		self.frame += 1
		if self.frame >= len(self.framesU):
			self.frame = 0
		print(self.frame + 1)
		self.shape(self.framesU[self.frame])
		# Set timer
		#wn.ontimer(self.jogUp, 100)

player = Player()




#keyboard binding
wn.listen()
wn.onkeypress(player.jogRight, "Right")
wn.onkeypress(player.jogUp, "Up")


while True:
	print("main loop")
	wn.update()

wn.mainloop()
