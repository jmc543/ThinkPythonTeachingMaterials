import math

def mysqrt(a):
    # returns estimated value of square root of x e.g. section 7.5
    x = 2  # just picking an initial guess
    epsilon = 0.0000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

def test_square_root():
    print(' a ', ' mysqrt(a) ', ' math.sqrt(a) ', ' diff ')
    print(' - ', ' --------- ', ' ------------ ', ' ---- ')
    for i in range(1, 10):
        mysqrt_result = mysqrt(i)
        mathsqrt_result = math.sqrt(i)
        diff = abs(mysqrt_result - mathsqrt_result)
        print(i, mysqrt_result, mathsqrt_result, diff)

if __name__ == '__main__':
    test_square_root()
