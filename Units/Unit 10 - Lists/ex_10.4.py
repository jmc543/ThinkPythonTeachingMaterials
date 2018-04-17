def chop(input_list):
    del input_list[0]
    del input_list[-1]
    return None

if __name__ == '__main__':
    t = [1, 2, 3, 4, 6, 7, 8]
    print(t)
    chop(t)
    print(t)
