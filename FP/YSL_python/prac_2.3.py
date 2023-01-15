import random

y = random.randint(0, 100)

print("\n\tGuess a magic number between 0 and 100")

while True:
    n = int(input("\tEnter your guess : "))
    if n == y:
        print("\tYes, the number is {}".format(str(n)))
        break
    elif n > y:
        print("\tYour guess is too high!")
    elif n < y:
        print("\tYour guess is too low!")
