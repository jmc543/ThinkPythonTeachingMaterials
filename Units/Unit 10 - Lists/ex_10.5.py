def is_sorted(input_list):
    sorted_list = input_list[:]
    sorted_list.sort()
    return input_list == sorted_list

if __name__ == '__main__':
    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))
