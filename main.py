import time
import os
from Classes.Dealer import Dealer
import Functions


cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
         '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

deck = list(4*('2', '3', '4', '5', '6', '7', '8', '9', '10',
               'Jack', 'Queen', 'King', 'Ace'))


def cls():
    """
    Commented out - bootleg "clear console" for Pycharm,
    use while writing, and switch to "os.system..." line when
    packing into .exe

    for getting coordinates:
    time.sleep(2)
    print(pyautogui.position())

    launch program, and move cursor to the simulated console window,
    after 2s you'll get coordinates to put as pyautogui.click() arguments
    :return:
    """

    # time.sleep(0.1)
    # pyautogui.click(x=778, y=832)
    # pyautogui.hotkey('ctrl', 'l')

    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:

        """
        Introducing the Player, and initialing the Dealer
        """

        player = Functions.introduction()
        buy_in = player.chips
        dealer = Dealer()
        cls()

        """
        Game Starts
        """

        print("Let The Game Begin")
        time.sleep(2)
        cls()
        gamestate = 'BEGINNING'

        while True:

            """
            Loop of the game, breaks when player decides to stop playing,
            or when he depletes all his chips
            """

            Functions.shuffle_deck(deck)
            bet = 0

            while True:

                """
                Player places a bet and draws cards until Bust, or Stop
                """

                try:
                    bet = int(input("Place your bet: "))
                    if bet > player.chips:
                        raise TypeError
                except TypeError or ValueError:
                    print("Wrong bet")
                    continue
                else:
                    break

            """
            2 cards are given to player and dealer, player shows both his cards,
            dealer only the first, if player doesn't win with a blackjack,
            game moves to PLAYER DRAWS phase
            """

            cls()
            gamestate = Functions.deal(player, dealer, deck, cards)
            Functions.table_state(gamestate, player, dealer, cards)

            if gamestate != "BLACKJACK":

                """
                Player draws cards
                """

                gamestate = Functions.player_draws(deck, player, cards)

                """
                Checking if Player has busted, and should game move to
                DEALER DRAWS phase
                """

                time.sleep(2)
                cls()
                if gamestate == 'DEALER DRAWS':

                    """
                    Dealer shows his second card and starts drawing until Bust, or Victory
                    """

                    Functions.table_state(gamestate, player, dealer, cards)
                    print()
                    gamestate = Functions.dealer_draws(deck, dealer, player, cards)

            """
            Match ends, scores ale evaluated, and if players has chips left,
            he can play again, in this case cards go back to deck, and game
            moves back to betting phase
            """

            choice = Functions.end_of_match(gamestate, bet, player)

            if choice.casefold() == 'yes':
                deck = Functions.new_card_deck(player, dealer)
                continue
            else:
                break

        """
        If Player decided to stop playing, or run out of chips, game is ended,
        final scores are shown (if he ultimately lost or gained chips while playing
        and he can decide if he wants to try again, with new buy-in and new name
        """

        play_again = Functions.end_of_game(buy_in, player)

        if play_again.casefold() == 'yes':
            cls()
            continue
        else:
            cls()
            break

    print('Hope to see you again friend!')
    time.sleep(2)


if __name__ == '__main__':
    main()
