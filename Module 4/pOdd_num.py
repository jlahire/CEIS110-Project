'''
Enter 5 integers:
5 99 -44 0 12
0 5
1 99
2 -44
3 0
4 12
Numbers: 5 99 -44 0 12
Odd numbers: 5 99
Negative numbers: -44

'''


size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter {} integers:\n'.format(num))

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:')
    for i in numbers:
        print(i)

def print_odd_numbers(numbers):
    # Print all odd numbers
    print('Odd numbers:')
    for i in numbers:
        if (i % 2) != 0:
            print(i)

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')
    for i in numbers:
        if i < 0:
            print(i)

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
