import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, gui):
        self.gui = gui
        self.gui.title("Guessing Game")
        
        self.initialize_game()
        self.game_active = True
        
        self.setup_interface()
        
    def initialize_game(self):
        self.target_number = random.randint(1, 21)
        self.attempts = 0
    

    def setup_interface(self):
        self.prompt_label = tk.Label(self.gui, text="Enter your guess:")
        self.prompt_label.pack()
        
        self.input_field = tk.Entry(self.gui)
        self.input_field.pack()
        
        self.guess_button = tk.Button(self.gui, text="Guess", command=self.process_guess)
        self.guess_button.pack()
        
        self.restart_button = tk.Button(self.gui, text="Restart Game", command=self.restart_game)
        self.restart_button.pack()
        
        self.reveal_button = tk.Button(self.gui, text="Reveal Number", command=self.reveal_number)
        self.reveal_button.pack()
        
        self.quit_button = tk.Button(self.gui, text="Exit", command=self.gui.quit)
        self.quit_button.pack()
        
    def process_guess(self):
        user_input = self.input_field.get()
        
        if user_input.isnumeric():
            guess = int(user_input)
            self.evaluate_guess(guess)
        elif user_input == "x":
            self.game_active = False
            self.gui.quit()
        elif user_input == "n":
            self.prompt_new_game()
        elif user_input == "s":
            self.reveal_number()
        
        self.input_field.delete(0, tk.END)
    
    def evaluate_guess(self, guess):
        self.attempts += 1
        
        if guess == self.target_number:
            messagebox.showinfo("Result", f"You guessed correctly! It took you {self.attempts} attempts.")
            self.prompt_new_game()
        elif guess > self.target_number:
            messagebox.showinfo("Result", "Your guess is too high.")
        else:
            messagebox.showinfo("Result", "Your guess is too low.")

    
    def prompt_new_game(self):
        user_response = messagebox.askquestion("New Game", "Would you like to start a new game?")
        
        if user_response == "yes":
            self.initialize_game()
        elif user_response == "no":
            self.game_active = False
            self.gui.quit()
    
    def reveal_number(self):
        messagebox.showinfo("Secret Number", f"The hidden number is {self.target_number}.")
    
    def restart_game(self):
        self.initialize_game()
        messagebox.showinfo("Game Restarted", "The game has been restarted.")
        self.input_field.delete(0, tk.END)

def main():
    gui = tk.Tk()
    game_app = GuessingGame(gui)
    gui.mainloop()

if __name__ == "__main__":
    main()
