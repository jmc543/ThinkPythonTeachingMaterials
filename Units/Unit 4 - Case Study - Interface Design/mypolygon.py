import turtle
import time

bob = turtle.Turtle()

# bob is an object with type Turtle as defined in the turtle module:
print(bob)
time.sleep(3)

# drawing a square:
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)


# reset screen after 3 second pause:
time.sleep(3)
turtle.reset()
print('resetting screen')
turtle.resetscreen()


# drawing a square with a "for" loop:
for i in range(4):
	bob.fd(100)
	bob.lt(90)


# start drawing/moving:
turtle.mainloop()
# NOTE: mainloop() must be the last thing called in a Turtle program!
