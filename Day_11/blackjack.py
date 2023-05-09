import random
from art import logo
def deal_card():
    """return a random card from desk"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the card"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"

    if user_score == computer_score:
        return "Draw"

    elif computer_score == 0:
        return "Lose, opponent has Blackjat"
    elif user_score == 0:
        return "Win, with a Blackjat"
    elif user_score > 21:
        return "you went over You lose"
    elif computer_score > 21:
        return "you went over,You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "you lose"

def play_game():

    print(logo)

    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


