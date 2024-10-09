import random

def number_guess(num):
    if num == rand_num:
        print('{} is correct!'.format(num))
    elif num < rand_num:
        print('{} is too low. Random number was {}.'.format(num,rand_num))
    else:
        print('{} is too high. Random number was {}.'.format(num,rand_num))
    
if __name__ == "__main__":
    
    random.seed(900)
    rand_num = random.randint(1, 100)
    user_input = input()
    
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)   
    