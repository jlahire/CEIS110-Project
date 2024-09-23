# Retype and run, note incorrect behavior. 
# Then fix errors in the code, which should 
# print num_stars asterisks.

# while num_printed != num_stars:
#     print('*')

# Sample output with input: 3

# *
# *
# *

num_printed = int(input())

num_stars = 0

symbol = "*"

while num_printed != num_stars:
    num_stars += num_printed
    print(symbol * num_stars)