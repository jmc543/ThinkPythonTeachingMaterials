def fib(n):
	if n < 0:
		print("can't enter negative number!")
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


num = int(input("enter an integer: "))
print("Fibonacci sequence up to ", num, ":")
for i in range(num):
	print(fib(i))

