def is_divisible(x, y):
    # returns True if x is divisible by y
    return x % y == 0


def is_power(a, b):
    # returns True if a is a power of b
    # a must be divisible by b:
    if not is_divisible(a, b):
        return False
    elif a == b:
        return True
    else:
        return is_power(a/b, b)


if __name__ == '__main__':
    print(is_power(6, 2))
    print(is_power(8, 2))
