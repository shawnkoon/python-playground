import unittest
from .app import GuessingGame

class GuessingGameTester(unittest.TestCase):
    def setUp(self):
        self.test_case = ['abc']


    def test_guess_success(self):
        a = GuessingGame(self.test_case)
        self.assertEqual(a.guess('a'), True)
        self.assertEqual(a.guess('b'), True)
        self.assertEqual(a.guess('c'), True)


    def test_guess_failure(self):
        a = GuessingGame(self.test_case)
        self.assertEqual(a.guess('e'), False)
        self.assertEqual(a.guess('2'), False)
        self.assertEqual(a.guess(' '), False)


    def test_guess_duplicate(self):
        a = GuessingGame(self.test_case)
        self.assertEqual(a.guess('a'), True)
        self.assertEqual(a.guess('a'), False)


if __name__ == '__main__':
    unittest.main()
