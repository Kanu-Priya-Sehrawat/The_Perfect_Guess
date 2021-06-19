# The Perfect Guess

import random
def guessNumber(n, guess):
    if n == guess:
        print("Congrats!! You guess the number in the first go!! You are such a genius ")
        return
    guess_count = 1
    while guess != n:
        if guess<n:
            print("You guess the smaller number \nHint: Enter the larger number : ", end="")
            guess = int(input())
            guess_count = guess_count + 1
        elif guess>n:
            print("You guess the larger number \nHint: Enter the smaller number : ", end="")
            guess = int(input())
            guess_count = guess_count + 1
    
    print(f"Congrats!! You guess the number in the {guess_count} time.")

    with open("highScore.txt") as f:
        hiScore = f.read()
    with open("highScore.txt",'w') as f:
        if hiScore == "":
            f.write(str(guess_count))
        elif guess_count<int(hiScore):
            print("You broke the high score !!")
            f.write(str(guess_count))


print("******** Lets play The_Perfect_Guess game ********")
n = random.randint(1, 10)
guess = int( input("Enter the number from 1 and 10 : "))
guessNumber(n, guess)