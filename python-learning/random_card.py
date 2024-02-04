import random

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
faces = ['Jack", "Queen", "King', "Ace"]
numbered = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]


def draw():
    suit = random.choice(suits)
    card = random.choice(numbered + faces)

    return card + " of " + suit


print(draw())
