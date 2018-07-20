from .app import GuessingGame, BANNER_TEXT, ANSWERS

if __name__ == '__main__':
    print(BANNER_TEXT)
    a = GuessingGame(ANSWERS)
    print(a)

    while not a.is_game_over():
        char = input('\nPlease Guess a character! ')
        print()
        a.guess(char)
        print(a)

    a.print_result()
