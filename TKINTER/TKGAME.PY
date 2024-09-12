import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")
        
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
    
    def button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.show_winner()
            elif "" not in self.board:
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def show_winner(self):
        messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
        self.reset_board()

    def show_draw(self):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        self.reset_board()

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "_main_":
    root = tk.Tk()
    game = TicTacToe(root)
    
    root.mainloop()