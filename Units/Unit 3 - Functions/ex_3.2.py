# part 1.
def do_twice(f):
	f()
	f()

def print_spam():
	print('spam')

do_twice(print_spam)

# part 2.
def do_twice_modified(f, val):
	f(val)
	f(val)

# part 3.
def print_twice(bruce):
	print(bruce)
	print(bruce)

# part 4.
do_twice_modified(print_twice, 'spam')

# part 5. 
def do_four(f, val):
	do_twice_modified(f, val)
	do_twice_modified(f, val)


