def cumsum(num_list):
    result_list = []
    running_total = 0
    for num in num_list:
        running_total += num
        result_list += [running_total]
    return result_list

if __name__ == '__main__':
    print(cumsum([1, 2, 3]))
