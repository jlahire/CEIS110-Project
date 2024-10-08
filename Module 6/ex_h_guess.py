import random

def numer_guess(num):
    rand_num = random.seed(900)
    if num == rand_num:
        print('{} is correct!'.format(num))
    elif num < rand_num:
        print('{} is too low. Random number was {}.'.format(num,rand_num))
    else:
        print('{} is too high. Random number was {}.'.format(num,rand_num))
    
if __name__ == "__main__":
    random.seed(900)
    
    
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        numer_guess(num)
    