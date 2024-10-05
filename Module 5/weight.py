'''
(1) Prompt the user to enter four numbers, 
each corresponding to a person's weight in 
pounds. Store all weights in a list. Output 
the list. (2 pts)

Ex:

Enter weight 1:
236.0
Enter weight 2:
89.5
Enter weight 3:
176.0
Enter weight 4:
166.3
Weights: [236.0, 89.5, 176.0, 166.3]

(2) Output the average of the list's 
elements with two digits after the decimal 
point. Hint: Use a conversion specifier to 
output with a certain number of digits 
after the decimal point. (1 pt)

(3) Output the max list element with two 
digits after the decimal point. (1 pt)

Ex:

Enter weight 1:
236.0
Enter weight 2:
89.5
Enter weight 3:
176.0
Enter weight 4:
166.3
Weights: [236.0, 89.5, 176.0, 166.3]

Average weight: 166.95
Max weight: 236.00

(4) Prompt the user for a number between 1 
and 4. Output the weight at the user 
specified location and the corresponding 
value in kilograms. 1 kilogram is equal to 
2.2 pounds. (3 pts)

Ex:

Enter a list location (1 - 4):
3
Weight in pounds: 176.00
Weight in kilograms: 80.00

(5) Sort the list's elements from least 
heavy to heaviest weight. (2 pts)

Ex:

Sorted list: [89.5, 166.3, 176.0, 236.0]

Output the average and max weights as 
floating-point values with two digits after 
the decimal point, which can be achieved as 
follows:
print('{:.2f}'.format(your_value))
'''

# FIXME (1): Prompt for four weights. Add all weights to a list. Output list.

weights = []

weight_1 = float(input('Enter weight 1:\n'))
weights.append(weight_1)
weight_2 = float(input('Enter weight 2:\n'))
weights.append(weight_2)
weight_3 = float(input('Enter weight 3:\n'))
weights.append(weight_3)
weight_4 = float(input('Enter weight 4:\n'))
weights.append(weight_4)

print(f'Weights: {weights}\n')

# FIXME (2): Output average of weights.

avg_weight = sum(weights)/len(weights)
print('Average weight: {:.2f}'.format(avg_weight))

# FIXME (3): Output max weight from list.

m_weight = max(weights)
print('Max weight: {:.2f}\n'.format(m_weight))

# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.

location = int(input('Enter a list location (1 - 4):\n'))

weight_in_pounds = weights[location - 1]
weight_in_kilos = (weights[location - 1] / 2.2)

print('Weight in pounds: {:.2f}'.format(weight_in_pounds))
print('Weight in kilograms: {:.2f}\n'.format(weight_in_kilos))

# FIXME (5): Sort the list and output it.

weights.sort()
print(f'Sorted list: {weights}')