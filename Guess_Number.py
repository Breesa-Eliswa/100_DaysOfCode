#THE GUESSING GAME
import random
print("Lets play the game: GUESS THE NUMBER")

Upper_bound = input("Type a number:")
if Upper_bound.isdigit():
    Upper_bound = int(Upper_bound)
    if Upper_bound <= 0:
        print("NEXT TIME PLEASE ENTER A NUMBER GREATER THAN ZERO")
        quit()
else:
    print("Next time Please enter a NUMBER")
    quit()

random_number = random.randint(0,Upper_bound)
guesses = 0

while True:
    guesses+=1
    guess_num = input("Make a guesss ")
    if guess_num.isdigit():
        guess_num =int(guess_num)   
    else:
        print("Next time please enter a number")
        continue
    if guess_num==random_number:
        print("You got it!!")
        break
    elif guess_num > random_number:
        print("Your guess is above the right number")
    else:
        print("Your guess is below the right number")
print("You got in",guesses,"guessses")