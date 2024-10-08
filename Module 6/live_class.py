# create file variable
file_name = 'names.txt'

# get input from user
name = input('Enter name >> ')

# write to file - "a" to append, "w" to overwrite
out_file = open( file_name, "a")
out_file.write( name + "\n" ) # \n to drop to next line
out_file.close()

# open the file to read it
in_file = open ( file_name, 'r')

name_list = []

for line in in_file:
    name = line[:-1]
    name_list.append( name )
    
in_file.close()

print('\nClient List:')
for i in range( len(name_list) ):
    print( name_list[i])
    
