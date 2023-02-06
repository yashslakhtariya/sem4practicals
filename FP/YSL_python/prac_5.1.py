import random


def ysl_card():
    suit = ("Clubs", "Diamonds", "Heart", "Spades")
    rank = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King")
    y = random.randint(0, 51)
    return rank[y % 13], suit[y // 13]


suits = []
i = 1
while i >= 1:
    rank, suit = ysl_card()
    if suit not in suits:
        suits.append(suit)
    elif len(suits) == 4:
        print(f"Number of picks taken to get at least one card from each suit : {i-1}")
        break
    print("The card you picked is {0} of {1}".format(rank, suit))
    i = i+1
