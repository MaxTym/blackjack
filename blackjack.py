import random

class Card:


    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


    def __init__(self, num):
        self.suit = Card.suits[num%4]
        self.rank = Card.ranks[num//4]


    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:


    def __init__(self):
        self.cards = []
        for i in range(52):
            self.cards.append(Card(i))


    def __getitem__(self, index):
        return self.cards[index]


    def shuffle(self):
        random.shuffle(self.cards)


    def __repr__(self):
        return "".join(repr(self.cards))


d = Deck()
d.shuffle()
print(d)
