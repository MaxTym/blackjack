import random
import os


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
    print("Welcome to Blackjack!!!")
    d = Deck()
    d.shuffle()
    points = 0
    dealer_points = 0
    hand = []
    dealer_hand = []
    current_card = d[0]
    hand.append(current_card)
    d = (d[1:])
    current_card = d[0]
    dealer_hand.append(current_card)
    print("Dealer's hand: {} #".format(current_card))
    d = (d[1:])
    current_card = d[0]
    hand.append(current_card)
    get_points(hand)
    d = (d[1:])
    print("Your hand: {}".format(hand))
    points = get_points(hand)
    print("Your points: {}".format(points))
    current_card = d[0]
    dealer_hand.append(current_card)
    d = (d[1:])
    dealer_points = get_points(dealer_hand)
    if points < 21:
        while points < 22:
            hit = input("One more card? 'Y'/'n'\n").lower()
            if hit == 'y':
                current_card = d[0]
                hand.append(current_card)
                d = (d[1:])
                if check_for_ace(hand):
                    if adjust_ace_value(hand):
                        points = get_points(hand)
                    else:
                        points = get_points_a1(hand)
                else:
                    points = get_points(hand)
                print(current_card)
                print("Your hand: {}".format(hand))
                print("Your points: {}".format(points))
            elif hit == 'n':
                break
            else:
                continue
        else:
            print("You lose!\n You have {} points".format(points))
            print(hand)
            if play_again():
                main()
        while dealer_points < 17:
            current_card = d[0]
            dealer_hand.append(current_card)
            d = (d[1:])
            if check_for_ace(dealer_hand):
                if adjust_ace_value(dealer_hand):
                    points = get_points(dealer_hand)
                else:
                    dealer_points = get_points_a1(dealer_hand)
            else:
                dealer_points = get_points(dealer_hand)
        if dealer_points > 21:
            print("Congratulations!!! You won")
            print('Dealer points: {}'.format(dealer_points))
            print('Dealer cards: {}'.format(dealer_hand))
            print('Your points: {}'.format(points))
            print('Your cards: {}'.format(hand))
            if play_again():
                main()
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
        if play_again():
            main()
    elif points > 21:
        print("You lose")
        if play_again():
            main()
    else:
        print("You won!!!")
        if play_again():
            main()


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


def count_points(current_card):
    if current_card.rank == 'J' or current_card.rank == 'Q' or current_card.rank == 'K':
        points = 10
    elif current_card.rank == 'A':
        points = 11
    else:
        points = int(current_card.rank)
    return points


def get_points(hand):
    total = 0
    for i in hand:
        if i.rank == 'J' or i.rank == 'Q' or i.rank == 'K':
            points = 10
        elif i.rank == 'A':
            points = 11
        else:
            points = int(i.rank)
        total += points
    return total


def get_points_a1(hand):
    total = 0
    for i in hand:
        if i.rank == 'J' or i.rank == 'Q' or i.rank == 'K':
            points = 10
        elif i.rank == 'A':
            points = 1
        else:
            points = int(i.rank)
        total += points
    return total


def adjust_ace_value(hand):
    if get_total_of_non_ace_cards(hand) <= 10:
        return True


def get_total_of_non_ace_cards(hand):
    total = 0
    for i in hand:
        if i.rank != 'A':
            if i.rank == 'J' or i.rank == 'Q' or i.rank == 'K':
                points = 10
            else:
                points = int(i.rank)
            total += points
    print(total)
    return total


def play_again():
    while True:
        play_again = input("Anoher round? 'Y'/'n'").lower()
        if play_again == 'y':
            return True
            break
        elif play_again == 'n':
            exit()


def check_for_ace(hand):
    for i in hand:
        if i.rank == 'A':
            return True


def main():
    os.system('clear')
    deal()




main()
