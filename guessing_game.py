import random as r
#sdsd
guesses = 0
def hint():
    if int(guess) < random_number:
        print("Your guess was low!")
    if int(guess) > random_number:
        print("Your guess was high!")



high_number = int(input("Enter number:"))




random_number = r.randrange(high_number)

print(f"Enter number between 1-{high_number +1}")
while True:
    guesses +=1
    guess = int(input(f"Guess Here: "))
    if guess == random_number:
        print("You got it!")
        print(f"You guessed it in {guesses} guesses!")
        quit("bye")

    else:
        hint()









