import random

computer_number = None
guess_count = 0
finish_state = False


def init():
    global computer_number, guess_count
    computer_number = generate_random_number()
    guess_count = 0


def main():
    global computer_number, guess_count, finish_state
    init()
    finish_state = False
    while not finish_state:
        user_decision = user_input()
        if user_decision.isnumeric():
            guess = int(user_decision)
            is_guess_correct(guess)
        elif user_decision == "x":
            finish_state = True
        elif user_decision == "n":
            user_answer = start_new_game()
            if user_answer == "yes":
                init()
            elif user_answer == "no":
                finish_state = True
        elif user_decision == "s":
            print(f"The random number is {computer_number}")


def generate_random_number():
    return random.randint(1, 21)


def user_input():
    return input("Guess a number or type (x,n,s): ")


def is_guess_correct(guess):
    global computer_number, guess_count, finish_state
    if guess == computer_number:
        print("You guessed correctly")
        print(f"You guessed {guess_count} times")
        user_answer = start_new_game()
        if user_answer == "yes":
            init()
        if user_answer == "no":
            finish_state = True
    elif guess > computer_number:
        print("Your number is too high")
    else:
        print("Your number is too low")
    guess_count += 1


def start_new_game():
    user_answer = ""
    while not (user_answer == "yes" or user_answer == "no"):
        user_answer = input("Do you want to start a new game?")
    return user_answer


main()
