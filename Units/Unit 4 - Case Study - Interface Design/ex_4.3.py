import turtle
import math

bob = turtle.Turtle()

# 1.
def square(t):
	for i in range(4):
		t.fd(100)
		t.lt(90)

square(bob)
	
turtle.resetscreen()

# 2.
def square_with_length(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)

square_with_length(bob, 50)
square_with_length(bob, 100)
square_with_length(bob, 150)

turtle.resetscreen()

# 3.
def polygon(t, length, n):
	# exterior angles of n-sided regular polygon are 360/n degrees:
	ext_angle = 360 / n
	for i in range(n):
		t.fd(length)
		t.lt(ext_angle)

polygon(bob, 50, 4)  # square
polygon(bob, 60, 5)  # pentagon
polygon(bob, 70, 6)  # hexagon
polygon(bob, 80, 7)  # septagon
polygon(bob, 90, 8)  # octagon

turtle.resetscreen()

# 4.
def circle(t, r):
	circumference = 2 * math.pi * r
	n = 100  # higher number means the approximation will be closer to a circle, but the drawing will take longer to complete
	length = circumference / n
	polygon(t, length, n)

circle(bob, 50)
circle(bob, 75)
circle(bob, 100)
circle(bob, 125)
circle(bob, 150)

turtle.resetscreen()

# 5.
def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = angle / n

	for i in range(n):
		t.fd(step_length)
		t.lt(step_angle)

arc(bob, 50, 180)
arc(bob, 60, 180)
arc(bob, 70, 180)
arc(bob, 80, 180)
arc(bob, 90, 180)
arc(bob, 100, 180)
arc(bob, 110, 180)
arc(bob, 120, 180)
arc(bob, 130, 180)
arc(bob, 140, 180)
arc(bob, 150, 180)

turtle.mainloop()
