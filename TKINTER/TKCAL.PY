import tkinter as tk
from math import sin, cos, tan, log, radians
class Calc:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.mode = "simple"  
        self.entry = tk.Entry(root, width=20, font=('Arial', 18), bd=5, insertwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.create_buttons()
        self.create_scientific_buttons()
        self.hide_scientific_buttons()
    def create_buttons(self):
        buttons = [
            'AC', '+', '-', '*',
            '7', '8', '9', '/',
            '4', '5', '6', '**2',
            '1', '2', '3', '**3',
            '0', '.', '%', '='
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.root, text=button, padx=20, pady=20, bg='white', fg='black', 
                      command=lambda b=button: self.click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        tk.Button(self.root, text="Sci", padx=20, pady=20, bg='blue', fg='white',
                  command=self.toggle_mode).grid(row=row_val, column=col_val)

    def create_scientific_buttons(self):
        self.sci_buttons = [
            ('cos', cos), ('sin', sin), ('tan', tan), ('log', log)
        ]
        row_val = 1
        col_val = 4
        for (text, func) in self.sci_buttons:
            btn = tk.Button(self.root, text=text, padx=20, pady=20, bg='red', fg='white', 
                            command=lambda f=func: self.scientific_calc(f))
            btn.grid(row=row_val, column=col_val)
            setattr(self, f"btn_{text}", btn)
            row_val += 1
    def click(self, value):
        if value == '=':
            try:
                self.entry.insert(tk.END, f" = {eval(self.entry.get())}")
            except Exception as e:
                self.entry.insert(tk.END, " Error")
        elif value == 'AC':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, value)
    def scientific_calc(self, func):
        try:
            value = float(self.entry.get())
            result = func(radians(value)) if func != log else func(value)
            self.entry.insert(tk.END, f" = {result}")
        except Exception as e:
            self.entry.insert(tk.END, " Error")
    def toggle_mode(self):
        if self.mode == "simple":
            self.show_scientific_buttons()
            self.mode = "scientific"
        else:
            self.hide_scientific_buttons()
            self.mode = "simple"
    def show_scientific_buttons(self):
        for text, _ in self.sci_buttons:
            getattr(self, f"btn_{text}").grid()
    def hide_scientific_buttons(self):
        for text, _ in self.sci_buttons:
            getattr(self, f"btn_{text}").grid_remove()
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calc(root)
    root.mainloop()
