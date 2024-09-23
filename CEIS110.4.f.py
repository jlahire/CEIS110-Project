'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between 
text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so 
on. chr(99) is 'c', etc.
'''

# Modify the program to include two-character 
# .com names, where the second character can 
# be a letter or a number, e.g., a2.com. Hint: 
# Add a second while loop nested in the outer 
# loop, but following the first inner loop, 
# that iterates through the numbers 0-9.

print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
number = 0

while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
        if letter2a >=9:
            letter2a == 0
        while letter2a <= 9:  # Inner loop 2
            print('{}{}.com'.format(letter1, letter2a))
            letter2a += 1

    letter1 = chr(ord(letter1) + 1)