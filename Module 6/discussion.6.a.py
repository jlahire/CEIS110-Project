'''
Topic 1: What is the difference between a syntax, logic, and runtime error?
'''
# def s_error():
    # Syntax Error
    # print('hello world!'
# s_error()


def add_numbers(a, b):
    return a - b

def l_error():
    # Logic Error
    added_numers = add_numbers(5,3)
    print(added_numers)
# l_error()


def divide_numbers(a, b):
    return a / b

def rt_error():
    # Runtime Error
    divided_numbers = divide_numbers(10, 0)
    print(divided_numbers)
# rt_error()