'''
The following (unfinished) program implements a digital 
line queuing system for an amusement park ride. The system 
allows a rider to reserve a place in line without actually 
having to wait. The rider simply enters a name into a 
program to reserve a place. Riders that purchase a VIP pass 
get to skip past the common riders up to the last VIP rider 
in line. VIPs board the ride first. (Considering the average 
wait time for a Disneyland ride is about 45 minutes, this 
might be a useful program.) For this system, an employee 
manually selects when the ride is dispatched (thus removing 
the next riders from the front of the line).

Complete the following program, as described above. Once 
finished, add the following commands:

******** The rider can enter a name to find the current position in 
line. (Hint: Use the list.index() method.)

******** The rider can enter a name to remove the rider from the line.

input(s):

1
Frank
4
1
Bob
3
4
5

'''

riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) Find rider position.\n'
        '(6) Remove rider.\n'
        '(7) Exit.\n\n')

user_input = input(menu).strip().lower()

while user_input != '7':
    if user_input == '1':  # Add rider 
        name = input('Enter name:').strip().lower()
        print(name)
        line.append(name)

    elif user_input == '2':  # Add VIP
        name = input('Enter name:').strip().lower()
        print(name)
        line.insert(num_vips, name)
        num_vips += 1

    elif user_input == '3':  # Dispatch ride
        del line[:riders_per_ride]
        num_vips = max(0, num_vips - riders_per_ride)


    elif user_input == '4':  # Print riders waiting in line
        print('{} person(s) waiting:'.format(len(line)), line)
    
    elif user_input == '5':  # Find rider position in line
        name = input('Enter rider name:').strip().lower()
        if name in line:
            print(f'{name} is at position {line.index(name) +1}.')
        else:
            print(f'{name} is not in the line.')
    
    elif user_input == '6':  # Remove rider from line
        name = input('Enter rider name:').strip().lower()
        if name in line:
            line.remove(name)
            num_vips = max(0, num_vips - 1)
            print(f'{name} removed from line.')
        else:
            print(f'{name} not in the line.')

    else:
        print('Unknown menu option')

    user_input = input('Enter command: ').strip().lower()
    print(user_input)
