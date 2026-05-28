import random
import tkinter as tk

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    # Fixed the indentation/line continuation here:
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!" 

class RockPaperScissorsGUI:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.tie_count = 0
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.window.resizable(False, False)

        self.status_label = tk.Label(self.window, text="Choose Rock, Paper, or Scissors.", font=("Arial", 14), pady=10)
        self.status_label.pack()

        self.score_label = tk.Label(self.window, text=self._score_text(), font=("Arial", 12), pady=5)
        self.score_label.pack()

        self.choice_frame = tk.Frame(self.window)
        self.choice_frame.pack(pady=10)

        for choice in ['rock', 'paper', 'scissors']:
            button = tk.Button(
                self.choice_frame,
                text=choice.capitalize(),
                width=10,
                font=("Arial", 12),
                command=lambda c=choice: self.play(c)
            )
            button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 12), pady=10)
        self.result_label.pack()

        self.reset_button = tk.Button(self.window, text="Reset", width=10, font=("Arial", 10), command=self.reset_scores)
        self.reset_button.pack(pady=(0, 10))

    def _score_text(self):
        return f"Player: {self.player_score}  Computer: {self.computer_score}  Ties: {self.tie_count}"

    def play(self, player_choice):
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        self.status_label.config(text=f"You chose {player_choice}. Computer chose {computer_choice}.")
        self.result_label.config(text=result)

        if result == "You win!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        else:
            self.tie_count += 1

        self.score_label.config(text=self._score_text())

    def reset_scores(self):
        self.player_score = 0
        self.computer_score = 0
        self.tie_count = 0
        self.score_label.config(text=self._score_text())
        self.status_label.config(text="Choose Rock, Paper, or Scissors.")
        self.result_label.config(text="")

    def run(self):
        self.window.mainloop()


def main():
    gui = RockPaperScissorsGUI()
    gui.run()


if __name__ == "__main__":
    main()