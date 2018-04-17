def nested_sum (int_list_list):
    total = 0
    for nested_list in int_list_list:
        total += sum(nested_list)
    return total

if __name__ == '__main__':
    print(nested_sum(([1,2,3], [3,4], [5])))
