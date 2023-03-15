## importing the random number and defining the  values
import random
randNumber = random.randint(1, 100)
guesses = 0
userGuess = None

## using while loop for runing the program repeatedly until user guessed the right number
while userGuess != randNumber:
    userGuess = int(input("Enter your guess:\n"))
    guesses += 1

    if userGuess < randNumber:
        print("You guessed it wrong! Please enter a larger number.")
    elif userGuess > randNumber:
        print("You guessed it wrong! Please enter a smaller number.")
    else:
        print("Congratulations! You guessed it right.")


## printing the total guesses of user
print(f"You guessed the number in {guesses} guesses.")

# updating highscores in another file
with open("highscore.txt", "r") as f:
    highscore = int(f.read())

if guesses < highscore:
    print("You have just broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))