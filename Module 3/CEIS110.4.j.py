


num_rows = int(input())
num_cols = int(input())

for row in range(1, num_rows + 1):
    letter = 'A'
    for col in range(num_cols):
        print('{}{}'.format(row, letter), end=' ')
        letter = chr(ord(letter) + 1)
print()