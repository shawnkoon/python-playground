import unittest
from .app import password_gen
from string import (
    ascii_lowercase as lower_let,
    ascii_uppercase as upper_let,
    punctuation,
    digits
)
from random import choice

class PasswordGenTest(unittest.TestCase):
    def test_password_gen(self):
        psw_1 = password_gen()
        self.assertEqual(any([char in lower_let for char in psw_1]), True, 'Lowercase letter not found in password.')
        self.assertEqual(any([char in upper_let for char in psw_1]), True, 'Uppercase letter not found in password.')
        self.assertEqual(any([char in digits for char in psw_1]), True, 'Number not found in password.')
        self.assertEqual(any([char in punctuation for char in psw_1]), True, 'Special char or punctuation mark not found in password.')



if __name__ == '__main__':
    unittest.main()
