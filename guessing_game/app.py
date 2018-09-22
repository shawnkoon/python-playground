import time
import random
from string import ascii_lowercase

BANNER_TEXT = r"""
           ____      ____      __                                     _
          |_  _|    |_  _|    [  |                                   / |_
            \ \  /\  / /.---.  | |  .---.  .--.  _ .--..--.  .---.  `| |-' .--.
             \ \/  \/ // /__\\ | | / /'`\] .'`\ [ `.-. .-. |/ /__\\  | | / .'`\ \
              \  /\  / | \__., | | | \__.| \__. || | | | | || \__.,  | |,| \__. |
               \/  \/   '.__.'[___]'.___.''.__.'[___||__||__]'.__.'  \__/ '.__.'
   ______                              _                     ______
 .' ___  |                            (_)                  .' ___  |
/ .'   \_|__   _   .---.  .--.  .--.  __  _ .--.   .--./) / .'   \_| ,--.  _ .--..--.  .---.
| |   ___[  | | | / /__\\( (`\]( (`\][  |[ `.-. | / /'`\; | |   ____`'_\ :[ `.-. .-. |/ /__\\
\ `.___]  | \_/ |,| \__., `'.'. `'.'. | | | | | | \ \._// \ `.___]  // | |,| | | | | || \__.,
 `._____.''.__.'_/ '.__.'[\__) )\__) )___|___||__].',__`   `._____.'\'-;__[___||__||__]'.__.'
                                                 ( ( __))
"""

ANSWERS = [
    'cat', 'dog', 'whale', 'shark', 'elephant',
    'bird', 'chicken', 'honeybadger', 'lion', 'tiger',
    'bear', 'horse', 'rabbit', 'wolf', 'kangaroo',
    'monkey', 'hippopotamus', 'goat', 'squirrel', 'giraffe'
]

class GuessingGame:
    def __init__(self, word_list, total_lives = 5):
        self.answer = random.choice(word_list)
        self.user_guess = ['?' for _ in self.answer]
        self.correct_count = 0

        self.total_lives = total_lives
        self.current_lives = total_lives
        self.tried_pool = set()


    def __str__(self):
        res = self.user_guess.__str__() + '\n'
        res += 'Lives: '
        for i in range(self.total_lives, 0, -1):
            if i > self.current_lives:
                res += u'\u2661 '
            else:
                res += u'\u2665 '

        return res


    def guess(self, char):
        char = char.lower()
        res = False

        if char not in ascii_lowercase or char == '':
            print('[Error]: Please enter a valid english letter.')
            return res

        if char in self.tried_pool:
            print('You\'ve already tried character \'{}\'.'.format(char))
            return res

        if char in self.answer:
            count = 0
            for i, c in enumerate(self.answer):
                if c == char:
                    count += 1
                    self.user_guess[i] = char
                    self.correct_count += 1
            print('Nice, You found {} letters.'.format(count))
            res = True
        else:
            print('Oh no >:( no character {} found!'.format(char))
            self.current_lives -= 1

        self.tried_pool.add(char)
        return res


    def is_game_over(self):
        if self.current_lives == 0 or len(self.answer) == self.correct_count:
            return True
        return False


    def print_result(self):
        print()
        if self.current_lives == 0:
            print('==================================================')
            print('Oh no... the answer was \'{}\''.format(self.answer))
            print('==================================================')
            return True
        else:
            print('==================================================')
            print('Nice! it took you {} guess! :O'.format(len(self.tried_pool)))
            print('==================================================')
            return False


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

