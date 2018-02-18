def eval_loop():
    print("enter 'done' when complete")
    user_input = input('>')
    eval_result = 0
    while user_input != 'done':
        eval_result = eval(user_input)
        print(eval_result)
        user_input = input('>')
    print('exiting')
    return eval_result


if __name__ == '__main__':
    eval_loop()
