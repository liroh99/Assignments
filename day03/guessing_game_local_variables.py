import random

def init():
    return generate_random_number(), 0

def main():
    finish_state = False
    computer_number, guess_count = init()

    while not finish_state:
        user_decision = user_input()
        if user_decision.isnumeric():
            guess = int(user_decision)
            computer_number, guess_count, finish_state = is_guess_correct(computer_number, guess, guess_count)
        elif user_decision == "x":
            finish_state = True
        elif user_decision == "n":
            user_answer = start_new_game()
            if user_answer == "yes":
                computer_number, guess_count = init()
            elif user_answer == "no":
                finish_state = True
        elif user_decision == "s":
            print(f"The random number is {computer_number}")

def generate_random_number():
    return random.randint(1, 21)

def user_input():
    return input("Guess a number or type (x,n,s): ")

def is_guess_correct(computer_number, guess, guess_count):
    finish_state = False
    guess_count += 1

    if guess == computer_number:
        print("You guessed correctly")
        print(f"You guessed {guess_count} times")
        user_answer = start_new_game()
        if user_answer == "yes":
            return init() + (finish_state,)
        elif user_answer == "no":
            finish_state = True
    elif guess > computer_number:
        print("Your number is too high")
    else:
        print("Your number is too low")

    return computer_number, guess_count, finish_state

def start_new_game():
    user_answer = ""
    while user_answer not in ("yes", "no"):
        user_answer = input("Do you want to start a new game? (yes/no): ")
    return user_answer

main()
