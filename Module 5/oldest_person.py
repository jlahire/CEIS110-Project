
'''
Consider the following program that allows a user 
to print the age of the Nth oldest known person to 
have ever lived. Note: The ages are in a list sorted 
from oldest to youngest.

1. Modify the program to print the correct ordinal 
number ("1st", "2nd", "3rd", "4th", "5th") instead 
of "1th", "2th", "3th", "4th", "5th".
2. For the oldest person, remove the ordinal number 
(1st) from the print statement to say, "The oldest 
person lived 122 years".

Reminder: List indices begin at 0, not 1, thus the 
print statement uses oldest_people[nth_person-1], 
to access the nth_person element (element 1 at 
index 0, element 2 at index 1, etc.).
'''


def suffix(nth_person):
    return {1:'st', 2:'nd', 3:'rd'}.get(nth_person, 'th')

oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

while True:

    nth_person = int(input('Enter N (1-5): '))

    if (nth_person >= 1) and (nth_person <= 5):
        if nth_person == 1:
            print('The oldest person lived {} years'.format(oldest_people[nth_person-1]))
        else:
            print(f'The {nth_person}{suffix(nth_person)} oldest person lived {oldest_people[nth_person-1]} years')
        break
    else:
        print("Enter a number 1-5.")
        