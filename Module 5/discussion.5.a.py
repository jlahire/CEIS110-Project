'''
Topic 1:
How would you create a shopping list in Python?
'''

import datetime
from datetime import date
    
def shopping_list():
    shopping_list = []
    
    while True:
        item = input("Enter an item (or press enter to finish): ").strip()
        if item == "":
            break
        shopping_list.append(item)
    
    print("\nYour shopping list:")
    for item in shopping_list:
        print(f"[] {item}")

shopping_list()
print("Michael Pabst", date.today())


