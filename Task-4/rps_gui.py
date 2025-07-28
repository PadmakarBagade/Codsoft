import tkinter as tk
from tkinter import messagebox
import random

# Game logic
def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(choices)
    result_text.set(f"Computer chose: {comp_choice.capitalize()}")

    if user_choice == comp_choice:
        outcome.set("It's a Tie! 🤝")
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'scissors' and comp_choice == 'paper') or \
         (user_choice == 'paper' and comp_choice == 'rock'):
        outcome.set("You Win! 🎉")
        user_score += 1
    else:
        outcome.set("Computer Wins! 💻")
        comp_score += 1

    score_text.set(f"You: {user_score}  |  Computer: {comp_score}")

    # Ask if user wants to play another round
    ask_next_round()

# Ask for next round
def ask_next_round():
    response = messagebox.askyesno("Play Again?", "Do you want to play another round?")
    if not response:
        root.quit()

# Reset the game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_text.set("Game restarted! Make your move.")
    outcome.set("")
    score_text.set("You: 0  |  Computer: 0")

# Initialize
choices = ['rock', 'paper', 'scissors']
user_score = 0
comp_score = 0

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

title = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=20)

# Buttons for user choice
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack()

tk.Button(button_frame, text="🪨 Rock", width=10, command=lambda: play('rock')).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="📄 Paper", width=10, command=lambda: play('paper')).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="✂️ Scissors", width=10, command=lambda: play('scissors')).grid(row=0, column=2, padx=10, pady=10)

# Results
result_text = tk.StringVar()
outcome = tk.StringVar()
score_text = tk.StringVar()
result_text.set("Make your move!")
outcome.set("")
score_text.set("You: 0  |  Computer: 0")

tk.Label(root, textvariable=result_text, font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
tk.Label(root, textvariable=outcome, font=("Arial", 16, "bold"), fg="#0066cc", bg="#f0f0f0").pack(pady=5)
tk.Label(root, textvariable=score_text, font=("Arial", 14), fg="green", bg="#f0f0f0").pack(pady=10)

# Replay and Exit buttons
control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack(pady=15)

tk.Button(control_frame, text="🔄 Replay Game", command=reset_game, bg="#ffa500", fg="white", font=("Arial", 12), width=15).grid(row=0, column=0, padx=10)
tk.Button(control_frame, text="❌ Exit Game", command=root.quit, bg="red", fg="white", font=("Arial", 12), width=15).grid(row=0, column=1, padx=10)

# Start GUI loop
root.mainloop()
