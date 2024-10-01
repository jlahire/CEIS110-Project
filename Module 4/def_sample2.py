#this function will display a message. 

# The message is passed to the function as an argument
def print_welcome(message):
    print(message)
    print()
    
def main():
    message="Welcome to our program!"
    print_welcome(message)
    
#The following code checks whether the 
# current module is the main module
if __name__ =="__main__":
    main();