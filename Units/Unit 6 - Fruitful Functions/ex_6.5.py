def gcd(a, b):
    # returns the greatest common denominator of a and b
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


if __name__ == '__main__':
    print(gcd(120, 48))
    print(gcd(99, 31))
    print(gcd(499494, 232902))

