import random

number=random.randint(1,21)
count=1
while True: 
    guess=int(input("Guess a number: "))
    if guess==number:
        print("You guessed correctly")
        break
    elif guess>number:
        print("Your number is too high")
    else: 
        print("Your number is too low")
    count+=1
print (f"You guessed {count} times")

    
