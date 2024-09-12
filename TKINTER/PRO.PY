XXXimport random
import time
from tkinter import *
# List of names
names = ["virat", "Emma", "joy", "Ava", "William", "warner", "James", "dev", "dhoni", "eve"]

root = Tk()

def generate_random_name():
    time.sleep(2) 
    random_name = random.choice(names)
    label2 = Label(root, text=random_name).pack()

root.geometry("500x500")
root.title("Tkinter")

Label1 = Label(root, text="").pack()
userInput = StringVar()
entry = Entry(root, textvariable=userInput).pack()

Button1 = Button(root, text="Generate Random Name", command=generate_random_name).pack()

root.mainloop()
