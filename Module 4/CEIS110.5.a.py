'''
Topic 1
1. Write a program that passes a variable to a function. 
2. Explain the benefits of incorporating a modular design 
   into a computer program. 
3. Would it be more efficient to write one large program? 
   Why or why not?
'''
from datetime import datetime
uName = input("Enter Name >> ")
def my_func(name, date):
    print(name, date)
my_func(name="{}".format(uName), date=datetime.today())


