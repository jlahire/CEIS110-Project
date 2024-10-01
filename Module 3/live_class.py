user_num = int(input())

if(user_num < 20) or (user_num > 98):
    print('Input must be 20-98')

else:
    # Flag
    digits_same = False

    while not digits_same:
        print(user_num)

        right_digit = user_num % 10 # ex: 93 % 10 = 3
        left_digit = user_num // 10 # ex: 93 // 10 = 9

        if right_digit == left_digit:
            digits_same = True

        user_num = user_num - 1