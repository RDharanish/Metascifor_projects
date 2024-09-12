import tkinter as  traceback
import random
window=traceback.Tk()
window.title("RANDOM GENERATOR")

def random1():
    label=traceback.Label(window,text=" ",bg='yellow')
    label.pack()
    r=random.randint(1,100)
    label.config(text=r)
button=traceback.Button(window,text="click",bg='green',command=random1)
button.pack()
window.mainloop()
