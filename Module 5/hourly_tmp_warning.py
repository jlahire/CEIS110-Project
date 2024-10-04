'''
Write a loop to print all elements in 
hourly_temperature. Separate elements 
with a -> surrounded by spaces.

Sample output for the given program 
with input: '90 92 94 95'

90 -> 92 -> 94 -> 95 

Note: 95 is followed by a space, then a newline. 
'''

user_input = input()
hourly_temperature = user_input.split()

''' Your solution goes here '''
for index in range(len(hourly_temperature)):
    print(hourly_temperature[index], end=' ')
    if index != (len(hourly_temperature)-1):
        print('->', end=' ')
print('')


