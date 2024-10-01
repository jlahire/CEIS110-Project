# (1) Prompt the user for an automobile service. Output the user's input. (1 pt)

# Ex:

# Enter desired auto service:
# Oil change
# You entered: Oil change

# (2) Output the price of the requested service. (4 pts)

# Ex:

# Enter desired auto service:
# Oil change
# You entered: Oil change
# Cost of oil change: $35

# The program should support the following services (all integers):

# Oil change -- $35
# Tire rotation -- $19
# Car wash -- $7
# If the user enters a service that is not listed above, then output the following error message:


# Error: Requested service is not recognized


# Start

o_change = 35
t_rot = 19
c_wash = 7
e_mess = 'Error: Requested service is not recognized'


a_service = input('Automobile service: ')
print(f'You entered: {a_service}')

# Process

if a_service == "Oil change":
    print(f'Cost of {a_service}: ${o_change}')
elif a_service == "Tire rotation":
    print(f'Cost of {a_service}: ${t_rot}')
elif a_service == "Car wash":
    print(f'Cost of {a_service}: ${c_wash}')
else:
    print(e_mess)
    
# End