def right_justify(s):
	input_string_length = len(s)
	spaces_needed = 70 - input_string_length
	output_string = ' ' * spaces_needed + s
	return output_string

# test:
print(right_justify('northstar'))
