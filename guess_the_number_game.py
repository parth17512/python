import random

random_number= random.randint(1,10)
guess= None

while guess != random_number:
    guess = int(input("guess the number between 1 and 10 :"))
    if guess< random_number:
        print("too low! try again")
    elif guess> random_number:
        print("too high! try again")

print("congratulation! you guessed the number .")