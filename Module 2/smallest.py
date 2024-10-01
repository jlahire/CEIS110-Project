# Write a program whose inputs are three integers, and whose output is the smallest of the three values.

# Ex: If the input is:

# 7
# 15
# 3
# the output is:

# 3

val_1 = input()
val_2 = input()
val_3 = input()

values = val_1, val_2, val_3

lst = values
lst = [int(x) for x in lst]
lst.sort(reverse=True)

print(lst[-1])