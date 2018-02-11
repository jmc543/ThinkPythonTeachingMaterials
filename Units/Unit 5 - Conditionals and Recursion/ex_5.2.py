# exercise 5.2, Fermat's Last Theorem

def check_fermat(a, b, c, n):
	if n > 2:
		a_to_the_n = a ** n
		b_to_the_n = b ** n
		c_to_the_n = c ** n
		if a_to_the_n + b_to_the_n == c_to_the_n:
			print("Holy smokes, Fermat was wrong!")
		else:
			print("No, that doesn't work\n")
	else:
		print("n must be greater than 2!")

def prompt_user_for_fermat_checks():
	print("going to check a^n + b^n = c^n (Fermat's Last Theorem)")
	a = int(input("enter value for a: \n"))
	b = int(input("enter value for b: \n"))
	c = int(input("enter value for c: \n"))
	n = int(input("enter value for n: \n"))
	check_fermat(a, b, c, n)

if __name__ == "__main__":
	print("<---- Press Ctrl-C to exit program ---->\n")
	while True:
		prompt_user_for_fermat_checks()
