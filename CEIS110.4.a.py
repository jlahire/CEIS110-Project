# Create a loop to display all even numbers from 0 to 100. 
# Describe the three elements that must be included in order 
# for a loop to perform correctly. What will happen if these 
# statements are not included? Provide examples.

# Lib

# Var

numMin = 0
numMax = 100

# Process

for num in range (numMin, numMax):
    if num % 2 == 0:
        print(num, end=" ")

# End