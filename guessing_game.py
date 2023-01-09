import random as r

high_number = input("Enter number: ")
random_number = r.randrange(0,int(high_number))

guess = input(f"Guess the number between 1-{high_number}: ")
