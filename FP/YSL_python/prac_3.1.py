import random

suit = ("Clubs", "Diamonds", "Heart", "Spades")

rank = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King")

y = random.randint(0, 51)

print("The card you picked is {0} of {1}".format(rank[y % 13], suit[y // 13]))
