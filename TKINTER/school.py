import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Registration Form")
label1 = tk.Label(root, text='Name :')
label1.pack()
e1 = tk.Entry(root)
e1.pack()
label2 = tk.Label(root, text="Age:")
label2.pack()
e2 = tk.Entry(root)
e2.pack()
label3 = tk.Label(root, text='Gender:')
label3.pack()
e3 = tk.Entry(root)
e3.pack()
label4 = tk.Label(root, text="Email:")
label4.pack()
e4 = tk.Entry(root)
e4.pack()
label5 = tk.Label(root, text="Phone :")
label5.pack()
e5 = tk.Entry(root)
e5.pack()
label6 = tk.Label(root, text="Grade :")
label6.pack()
e6 = tk.Entry(root)
e6.pack()
def submit():
    name = e1.get()
    age = e2.get()
    gender = e3.get()
    email = e4.get()
    phone = e5.get()
    grade = e6.get()
    if not all([name, age, gender, email, phone, grade]):
        messagebox.showerror('Error', 'Please fill all the fields')
    else:
        messagebox.showinfo('Success', 'Registration successful')
sub = tk.Button(root, text="Submit", command=submit)
sub.pack()
root.mainloop()

