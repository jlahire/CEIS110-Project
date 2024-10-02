print('some list things to remember.')
my_list = ['h', 'e', 'l', 'l', 'o']
print(my_list)
my_list[len(my_list):] = [' ', 'w', 'o', 'r', 'l', 'd', '.']
print(my_list)
my_list[11] = '!'
print(my_list)
del my_list[5]
print(my_list)
x = '5'
my_list.append(x)
print(my_list)
del my_list[-1]
print(my_list)
print(', '.join(my_list))
print(' '.join(my_list))
print(''.join(my_list))
my_list = [1, 2, 3]
print(my_list)
my_list.extend([4, 5, 6])
print(my_list)
my_list.insert(3, 'insert')
print(my_list)
my_list.remove('insert')
print(my_list)
val = my_list.pop()
print(val)
val = my_list.pop(0)
print(val)
my_list = [5, 3, 2, 6, 1, 4]
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
my_list = [54, 3, 19]
print(my_list)
print(my_list.index(3))
my_list = [5, 4, 5, 5, 6, 19]
print(my_list)
print(my_list.count(5))