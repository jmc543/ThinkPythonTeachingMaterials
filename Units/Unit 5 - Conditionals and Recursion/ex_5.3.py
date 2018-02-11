# exercise 5.3 in the textbook

def is_triangle(side_1, side_2, side_3):
	if side_1 > side_2 + side_3:
		print("No")
	elif side_2 > side_1 + side_3:
		print("No")
	elif side_3 > side_1 + side_2:
		print("No")
	else:
		print("Yes")

def prompt_user_to_check_triangle():
	s1 = int(input("side 1: "))
	s2 = int(input("side 2: "))
	s3 = int(input("side 3: "))
	is_triangle(s1, s2, s3)

if __name__ == "__main__":
	prompt_user_to_check_triangle()

