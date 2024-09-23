'''

Write a function shampoo_instructions() with parameter num_cycles. 
If num_cycles is less than 1, print "Too few.". 
If more than 4, print "Too many.". 
Else, print "N : Lather and rinse." num_cycles times, where N is the cycle number, followed by "Done.".

Sample output with input: 2

1 : Lather and rinse.
2 : Lather and rinse.
Done.
 
'''


def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.')
    else:
        i = 1
        while i <= num_cycles:
            print(i, ': Lather and rinse.')
            i = i + 1
        print('Done.')

user_cycles = int(input())
shampoo_instructions(user_cycles)