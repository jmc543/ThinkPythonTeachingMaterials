def print_column():
    print('+----+----+')

def print_row():
    print('|    |    |')

def do_four(f):
	f()
	f()
	f()
	f()

def print_rows():
	do_four(print_row)

def do_block():
    print_column()
    print_rows()

# part 1.
def print_block():
    do_block() 
    do_block() 
    print_column()

print_block()

# part 2.
def print_four_columns():
    print('+----+----+----+----+')

def print_four_column_row():
    print('|    |    |    |    |')

def print_four_column_rows():
	do_four(print_four_column_row)

def do_block_four_columns():
	print_four_columns()
	print_four_column_rows()

def print_four_by_four_block():
	do_four(do_block_four_columns)
	print_four_columns()

print_four_by_four_block()

