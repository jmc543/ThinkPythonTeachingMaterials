def ack(m, n):
	'''
	Ackermann function.
	(exercise 6.2 in textbook)
	'''
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ack(m-1, 1)
	else:
		return ack(m-1, ack(m, n-1) )

if __name__ == "__main__":
	# testing:
	print( ack(3,4) )  # should be 125

	#print( ack(4,5) )  # larger values of m and n cause the maximum recursion depth to be reached
