'''
Given num_rows and num_cols representing 
the number of rows and columns, write nested 
loops using range() to print a rectangle as 
shown in the example below.

Ex: If the input is 2 3, then the output is:
* * * 
* * * 

Note: The inner loop should be indented once 
to contain the inner print statement.

'''

num_rows = int(input())
num_cols = int(input())

for r in range(num_rows):
    for c in range(num_cols):
        print('*', end=' ')
    print()

