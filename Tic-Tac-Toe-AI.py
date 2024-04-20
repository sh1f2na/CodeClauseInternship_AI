import tkinter as tk
from tkinter import messagebox

# Define players
humanPlayer = 'X'
aiPlayer = 'O'

# Create the main Tkinter window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize the board
board = [' '] * 9

# Function to check for winning combinations
def winning(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if (board[i*3] == board[i*3+1] == board[i*3+2] == player) or \
           (board[i] == board[i+3] == board[i+6] == player):
            return True
    if (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True
    return False

# Function to handle a player's move
def player_move(idx):
    if board[idx] == ' ':
        button[idx].config(text=humanPlayer)
        board[idx] = humanPlayer
        if winning(humanPlayer):
            messagebox.showinfo("Tic Tac Toe", "You win!")
            root.quit()
        elif ' ' not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            root.quit()
        else:
            ai_move()

# Function to make AI move
def ai_move():
    best_score = float('-inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = aiPlayer
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    button[best_move].config(text=aiPlayer)
    board[best_move] = aiPlayer
    if winning(aiPlayer):
        messagebox.showinfo("Tic Tac Toe", "You lose!")
        root.quit()
    elif ' ' not in board:
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        root.quit()

# Minimax algorithm
def minimax(board, is_maximizing):
    if winning(aiPlayer):
        return 1
    elif winning(humanPlayer):
        return -1
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = aiPlayer
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = humanPlayer
                score = minimax(board, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Create buttons for the Tic Tac Toe grid
button = []
for i in range(9):
    button.append(tk.Button(root, text=' ', font=('Timesnewroman', 20), width=5, height=2,
                            command=lambda idx=i: player_move(idx)))
    button[i].grid(row=i // 3, column=i % 3)

# Start the game
root.mainloop()
