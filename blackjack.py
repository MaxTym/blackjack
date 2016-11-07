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


    def get_next_card(self):
        if self.current_position >= len(self.cards):
#             raise NoCardsLeftError
            return None
        out = self.cards[self.current_position]
        self.current_position += 1
        return out


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


def deal():
    d = Deck()
    d.shuffle()
    #print(d[0].rank)
    #print(d[1].rank)
    points = 0
    dealer_points = 0
    hand = []
    dealer_hand = []
    current_card = d[0]
    hand.append(current_card)
    d = (d[1:])
    points += count_points(current_card)
    current_card = d[0]
    dealer_hand.append(current_card)
    print("Dealer's hand: {}#".format(current_card))
    d = (d[1:])
    dealer_points += count_points(current_card)
    current_card = d[0]
    hand.append(current_card)
    d = (d[1:])
    points += count_points(current_card)
    print(hand)
    print(points)
    current_card = d[0]
    dealer_hand.append(current_card)
    d = (d[1:])
    dealer_points += count_points(current_card)
    if points < 21:
        while another_card():
            hand.append(d[0])
            current_card = d[0]
            d = (d[1:])
            points += count_points(current_card)
            print(points)
        while dealer_points <17:
            dealer_hand.append(current_card)
            d = (d[1:])
            dealer_points += count_points(current_card)
        if dealer_points > points:
            print("You lose")
        elif dealer_points == points:
            print("Its a draw")
        else:
            print("Congratulations!!! You won")
        print('Dealer points: {}'.format(dealer_points))
        print('Dealer cards: {}'.format(dealer_hand))
        print('Your points: {}'.format(points))
        print('Your cards: {}'.format(hand))
    elif points > 21:

        print("You lose")
    else:
        print("You won!!!")



def another_card():
    while True:
        hit = input("One more card? 'Y'/'n'\n").lower()
        if hit == 'y':
            return True
            break
        elif hit == 'n':
            return False
            break
        else:
            continue

def dealer_turn():
    dealer_points = 0


def count_points(current_card):
    if current_card.rank == 'J' or current_card.rank == 'Q' or current_card.rank == 'K':
        points = 10
    elif current_card.rank == 'A':
        points = 11
    else:
        points = int(current_card.rank)
    return points

deal()
#count_points()
