def generate_random_number():
    number=random.randint(1,21)
    return number

def user_input():
    guess = input("Guess a number: ")
    return guess

def is_guess_correct():
    number = generate_random_number()
    guess = user_input()
    new_game_token = False
    count=1
    flag  = "True"
    while flag == "True":
        if guess==number:
            print("You guessed correctly")
            print (f"You guessed {count} times")
            break 
        elif guess>number:
            print("Your number is too high")
        else: 
            print("Your number is too low")
        count+=1
        decesion = game_d()
        if decesion == 
    



def game_d():
    d = user_input()
    if d == 'x':
        return "false"
    if d == "n":
        d2 = user_input()
        if d2 == 'yes':
            return "maybe"
        else:
            return "no"
        
            

