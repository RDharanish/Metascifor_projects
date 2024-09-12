import tkinter as tk
from tkinter import colorchooser
from tkinter import ttk
class PaintApp:
            def __init__(self, root): 
                self.root = root
                self.root.title("Simple Paint App")
                self.root.geometry("800x600")

                self.pen_button = ttk.Button(root, text="Pen", command=self.use_pen)
                self.pen_button.grid(row=0, column=0)

                self.brush_button = ttk.Button(root, text="Brush", command=self.use_brush)
                self.brush_button.grid(row=1, column=1)

                self.color_button = ttk.Button(root, text="Color", command=self.choose_color)
                self.color_button.grid(row=2, column=1)

                self.eraser_button = ttk.Button(root, text="Eraser", command=self.use_eraser)
                self.eraser_button.grid(row=3, column=1)

                self.size_label = ttk.Label(root, text="Size:")
                self.size_label.grid(row=4, column=1)

                self.size_slider = ttk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
                self.size_slider.set(5)
                self.size_slider.grid(row=5, column=1)

                self.c = tk.Canvas(root, bg='white', width=800, height=550)
                self.c.grid(row=5, columnspan=6)

                self.old_x = None
                self.old_y = None
                self.pen_color = "black"
                self.eraser_on = False
                self.active_button = self.pen_button

                self.setup()

            def setup(self):
                self.c.bind('<B1-Motion>', self.paint)
                self.c.bind('<ButtonRelease-1>', self.reset)

            def use_pen(self):
                self.active_button = self.pen_button
                self.eraser_on = False

            def use_brush(self):
                self.active_button = self.brush_button
                self.eraser_on = False

            def choose_color(self):
                self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]

            def use_eraser(self):
                self.active_button = self.eraser_button
                self.eraser_on = True

            def paint(self, event):
                brush_width = self.size_slider.get()
                paint_color = 'white' if self.eraser_on else self.pen_color

                if self.old_x and self.old_y:
                    self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=brush_width, fill=paint_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE, splinesteps=36)

                self.old_x = event.x
                self.old_y = event.y

            def reset(self, event):
                self.old_x = None
                self.old_y = None

if __name__ == '__main__':
    root = tk.Tk()
    PaintApp(root)
    root.mainloop()


    