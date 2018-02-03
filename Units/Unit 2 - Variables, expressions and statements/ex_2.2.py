# NOTE: the students will just be using the IDLE interpreter as a calculator

# 1. Volume of sphere with radius 5:
pi = 3.14
radius = 5
volume = 4 / 3 * pi * radius ** 3  # the ** operator is exponentiation
print("Volume of sphere with radius 5 is ", volume)

# 2. Wholesale cost:
cover_price = 24.95
discount_percentage = 0.40
shipping_price_first = 3
shipping_price_rest = 0.75
num_copies = 60
book_cost = num_copies * cover_price * (1 - discount_percentage)
ship_cost = shipping_price_first + (num_copies - 1) * shipping_price_rest
total_cost = book_cost + ship_cost
print("Wholesale cost: ", total_cost)

