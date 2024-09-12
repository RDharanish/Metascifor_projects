# write a python program and create different functions to add, subtract, and multiply two numbers.
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y

user_input=int(input("ENTER THE OPERATION YOU WANT TO BE PERFORM: \n 1.addition,2.substraction 3.multiplication"))
x=int(input("ENTER FIRST NUMBER: "))
y=int(input("ENTER SECOND NUMBER: "))
if user_input==1:
    print(add())
elif user_input ==2:
    print(sub())
elif user_input==3:
    print(mul())
else:
    print("INVALID OPERATION ")



