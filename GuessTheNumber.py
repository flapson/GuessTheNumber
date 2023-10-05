import random

secretNumber=random.randint(1,20)
print("Im thinking of a Number between 1 and 20")
for guesses_taken in range (1,7):
    print("Take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is to low")
    elif guess > secretNumber:
        print("Your guess is to high")
    else:
        break
if guess == secretNumber:
    print("Good Job! You guessed my Number in " + str(guesses_taken)+" guesses.")
else:
    print("Nope,the Number i was thinking of was "+ str(secretNumber))
    


