import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    result_label.config(
        text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
    )

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Title label
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title.pack(pady=10)

# Buttons
rock_btn = tk.Button(root, text="Rock", width=10, command=lambda: play("Rock"))
paper_btn = tk.Button(root, text="Paper", width=10, command=lambda: play("Paper"))
scissors_btn = tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors"))

rock_btn.pack(pady=5)
paper_btn.pack(pady=5)
scissors_btn.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run app
root.mainloop()