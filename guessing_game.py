import random as r
#sdsddsdd

def hint():
    if int(guess) < random_number:
        print("Your guess was low!")
    if int(guess) > random_number:
        print("Your guess was high!")


high_number = int(input("Enter number: "))
random_number = r.randrange(high_number)
print(f"Enter number between 0-{high_number}")

while True:
    guess = int(input(f"Guess Here: "))
    if guess == random_number:
        print("You got it")
        break
