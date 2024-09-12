import tkinter as tk
from tkinter import*
from tkinter import messagebox
import json
class Quiz:
    def __init__(self):
        self.score=0
        self.cur_ques=0
        self.questions=self.load()
        self.root=tk.Tk()
        self.root.title("quiz")
        self.display()
    def load(self):
        with open("quiz.json") as file1:
            return json.load(file1)["questions"]
    def display(self):
        self.clear_screen()
        question=self.questions[self.cur_ques] 
        tk.Label(self.root,text=question["question"]).pack()
        self.varaibles=[]
        for option in question["options"]:
            var=tk.IntVar()
            tk.Radiobutton(self.root,text=option,variable=var,value=len(self.varaibles)).pack(anchor=tk.W)
            tk.Radiobutton(self.root, text=option, variable=var, value=len(self.varaibles)).pack(anchor=tk.W)
            self.varaibles.append(var)
        tk.Button(self.root, text="Next", command=self.check_answer).pack()
        tk.Button(self.root, text="Quit", command=self.root.destroy).pack()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def check_answer(self):
        question = self.questions[self.cur_ques]
        answer = question["answer"]
        for i in range(len(self.variables)):
            if self.varaibles[i].get() == 1 and i == answer:
                self.score += 1
        self.cur_ques += 1
        if self.cur_ques < len(self.questions):
            self.display()
        else:
            self.display_result()

    def display_result(self):
        self.clear_screen()
        messagebox.showinfo("Result", f"Your score is {self.score} out of {len(self.questions)}")
        self.root.destroy()

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start()
