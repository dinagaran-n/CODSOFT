import tkinter as tk
import random

# Colors and styles
BG_COLOR = "#2E2E2E"
FG_COLOR = "#FFFFFF"
BTN_BG = "#444"
BTN_HOVER = "#666"
WIN_COLOR = "#00FF00"
LOSE_COLOR = "#FF4C4C"
TIE_COLOR = "#F0E68C"
FONT_MAIN = ("Segoe UI", 14)
FONT_TITLE = ("Segoe UI", 18, "bold")

user_score = 0
computer_score = 0

# Game Logic
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(user_choice, computer_choice)

    label_user.config(text=f"You chose: {user_choice}")
    label_computer.config(text=f"Computer chose: {computer_choice}")
    label_result.config(text=result)

    if result == "You win!":
        label_result.config(fg=WIN_COLOR)
        user_score += 1
    elif result == "You lose!":
        label_result.config(fg=LOSE_COLOR)
        computer_score += 1
    else:
        label_result.config(fg=TIE_COLOR)

    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You win!"
    else:
        return "You lose!"

def on_enter(e):
    e.widget['background'] = BTN_HOVER

def on_leave(e):
    e.widget['background'] = BTN_BG

# Window Setup
window = tk.Tk()
window.title("Rock-Paper-Scissors Pro")
window.geometry("480x400")
window.config(bg=BG_COLOR)
window.resizable(False, False)

# Title
label_title = tk.Label(window, text="Rock-Paper-Scissors", font=FONT_TITLE, bg=BG_COLOR, fg="#00BFFF")
label_title.pack(pady=20)

# Frame for results
frame_results = tk.Frame(window, bg=BG_COLOR)
frame_results.pack(pady=10)

label_user = tk.Label(frame_results, text="You chose: ", font=FONT_MAIN, bg=BG_COLOR, fg=FG_COLOR)
label_user.grid(row=0, column=0, padx=10)

label_computer = tk.Label(frame_results, text="Computer chose: ", font=FONT_MAIN, bg=BG_COLOR, fg=FG_COLOR)
label_computer.grid(row=1, column=0, padx=10)

label_result = tk.Label(window, text="", font=("Segoe UI", 16, "bold"), bg=BG_COLOR)
label_result.pack(pady=10)

label_score = tk.Label(window, text="Score - You: 0 | Computer: 0", font=FONT_MAIN, bg=BG_COLOR, fg="#FFD700")
label_score.pack(pady=10)

# Button Frame
frame_buttons = tk.Frame(window, bg=BG_COLOR)
frame_buttons.pack(pady=15)

def create_button(text, command):
    btn = tk.Button(frame_buttons, text=text, width=12, font=FONT_MAIN,
                    bg=BTN_BG, fg=FG_COLOR, relief="flat", command=command)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

btn_rock = create_button("🪨 Rock", lambda: play("Rock"))
btn_paper = create_button("📄 Paper", lambda: play("Paper"))
btn_scissors = create_button("✂️ Scissors", lambda: play("Scissors"))

btn_rock.grid(row=0, column=0, padx=10)
btn_paper.grid(row=0, column=1, padx=10)
btn_scissors.grid(row=0, column=2, padx=10)

# Exit Button
btn_exit = tk.Button(window, text="❌ Exit", font=FONT_MAIN, bg="#8B0000", fg="white", command=window.destroy)
btn_exit.pack(pady=10)

# Run App
window.mainloop()
