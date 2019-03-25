import random
import time
from main import cls
from Classes.Player import Player
from Classes.Dealer import Dealer


def introduction():
    """
    Introducing a player, choosing name, and buy-in for the game
    :return:
    """

    print('Welcome to the Table')
    player_name = input("What's your name friend?: ")
    buy_in = input("Standard buy-in is 100 chips, would you like to buy more?(Yes/No): ")

    if buy_in.casefold() == 'yes':
        buy_in = int(input("How much then?: "))
    else:
        buy_in = 100

    return Player(player_name, buy_in)


def deal(player=None, dealer=None, deck=None, cards=None):
    """
    Dealing 2 cards to the player and the dealer

    :param cards:
    :param player:
    :param dealer:
    :param deck:
    :return:
    """

    if cards is None:
        cards = {}
    if deck is None:
        deck = []
    if player is None:
        player = Player('sample', 100)
    if dealer is None:
        dealer = Dealer()

    for man in player, dealer:
        man.take_cards(deck[0], deck[1])
        deck.pop(0)
        deck.pop(0)

    if (player.score(cards) == 21) or (player.cards[0] == player.cards[1] == 'Ace'):
        return "BLACKJACK"
    else:
        return "PLAYER DRAWS"


def shuffle_deck(deck=None):
    """
    Shuffling cards in the deck
    :param deck:
    :return:
    """

    if deck is None:
        deck = []

    print("Shufling deck...")
    time.sleep(3)
    random.shuffle(deck)
    cls()


def table_state(gamestate, player=None, dealer=None, cards=None):
    """
    Showing State of the game,
    player and dealer cards, and their scores
    :param gamestate:
    :param player:
    :param dealer:
    :param cards:
    :return:
    """

    if player is None:
        player = Player('sample', 100)
    if dealer is None:
        dealer = Dealer()

    if cards is None:
        cards = {}
    if gamestate == 'PLAYER DRAWS':
        print(f"Dealer's Open Card: '{dealer.cards[0]}'")
        dealer_score = cards[dealer.cards[0]]
        print(f"Dealer's Score: {dealer_score}")
    else:
        print("Dealer's cards are: ")
        for card in dealer.cards:
            print(f"'{card}'")
        print(f"Dealer's Score: {dealer.score(cards)}")

    print("\n\n")

    print("You Have: ")
    for card in player.cards:
        print(f"'{card}'")
    print(f"Your Score: {player.score(cards)}")
    print()


def player_draws(deck=None, player=None, cards=None):
    """
    Player Draws cards until he Busts, or decides to Stop
    :param deck:
    :param player:
    :param cards:
    :return:
    """

    if cards is None:
        cards = {}
    if deck is None:
        deck = []
    if player is None:
        player = Player('sample', 100)

    while True:
        choice = input('Hit or Stop?: ')
        if choice.casefold() == 'stop':
            return "DEALER DRAWS"
        elif choice.casefold() == 'hit':
            print(f"You draw: {deck[0]}")
            player.cards.append(deck[0])
            deck.pop(0)
            score = player.score(cards)
            if (score > 21 and 'Ace' not in player.cards) or score > 31:
                print("BUST!")
                return "BUST"
            elif score > 21 and 'Ace' in player.cards:
                score -= 10
            if score == 21:
                print("BLACKJACK")
                return "BLACKJACK"
            print(f"Your Score: {score}")
            print()
        else:
            continue


def dealer_draws(deck=None, dealer=None, player=None, cards=None):

    """
    Function for Dealer to draw cards,
    he draws till winning (by having higher or equal score to the player)
    or busting
    :param deck:
    :param dealer:
    :param player:
    :param cards:
    :return:
    """

    if cards is None:
        cards = {}
    if deck is None:
        deck = []
    if dealer is None:
        dealer = Dealer()
    if player is None:
        player = Player('sample', 100)

    dealer_score = dealer.score(cards)
    player_score = player.score(cards)
    if dealer_score >= player_score:
        return "DEALER WINS"

    time.sleep(2)
    while True:
        print(f"Dealer draws: {deck[0]}")
        dealer.cards.append(deck[0])
        deck.pop(0)
        dealer_score = dealer.score(cards)
        time.sleep(2)
        if (dealer_score > 21 and 'Ace' not in dealer.cards) or dealer_score > 31:
            print("DEALER BUST!")
            return "PLAYER WINS"
        elif dealer_score > 21 and 'Ace' in dealer.cards:
            dealer_score -= 10
        if dealer_score == 21 or dealer_score >= player.score(cards):
            print(f"Dealer's Score: {dealer_score}")
            print()
            print("DEALER WINS")
            return "DEALER WINS"

        print(f"Dealer's Score: {dealer_score}")
        print()


def end_of_match(gamestate, bet, player=None):

    """
    Function used when match has ended,
    checks who won, based on variable "gamestate"
    and increases or decreses players account acordingly
    gives option to play another match, or to end game and move to
    'end_of_game' function
    if player has depleted all his chips, automatically goes to "end_of_game'
    :param gamestate:
    :param bet:
    :param player:
    :return:
    """

    if player is None:
        player = Player('sample', 100)

    time.sleep(3)
    cls()
    if gamestate in ('BLACKJACK', 'PLAYER WINS'):
        player.chips += bet
        print(f"You won your bet, current balance {player.chips} chips")
    else:
        if player.chips > bet:
            player.chips -= bet
            print(f'You lost your bet, current balance {player.chips} chips')
        else:
            print("You don't have any more chips")
            print()
            player.chips = 0
            return 'No'
    return input("Play some more? (Yes/No): ")


def new_card_deck(player=None, dealer=None):

    """
    preparing fresh card deck, clearing player, and dealer cards
    :param player:
    :param dealer:
    :return:
    """

    if dealer is None:
        dealer = Dealer()
    if player is None:
        player = Player('sample', 100)

    player.cards.clear()
    dealer.cards.clear()
    cls()
    return list(4 * ('2', '3', '4', '5', '6', '7', '8', '9', '10',
                     'Jack', 'Queen', 'King', 'Ace'))


def end_of_game(buy_in, player=None):

    """
    Function ending the game
    gives a total sum up of won/lost chips,
    and gives option to start from the beginning(choosing name and buy-in,
    totally new player)
    :param buy_in:
    :param player:
    :return:
    """

    cls()
    if player is None:
        player = Player('sample', 100)

    chips = player.chips - buy_in
    if chips > 0:
        print(f"Thanks for playin' {player.name}. fortune favors you,\n"
              f"you won {chips} chips.")
    elif chips < 0:
        print(f"Thanks for playin' {player.name}. no luck today,\n"
              f"you lost {abs(chips)} chips.")
    else:
        print(f"Thanks for playin' {player.name},\n"
              "won nothing, lost nothing, not a bad deal.")
    print()
    return input("Would you like to try your luck in another game? (Yes/No): ")
