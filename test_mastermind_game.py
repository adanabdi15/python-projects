
import unittest
from mastermind_game import compare_codes

class TestMastermindGame(unittest.TestCase):
    def test_all_correct(self):
        secret = ['red', 'blue', 'green', 'yellow']
        guess = ['red', 'blue', 'green', 'yellow']
        self.assertEqual(compare_codes(secret, guess), (4, 0))

    def test_all_cows(self):
        secret = ['red', 'blue', 'green', 'yellow']
        guess = ['blue', 'red', 'yellow', 'green']
        self.assertEqual(compare_codes(secret, guess), (0, 4))

    def test_some_bulls_and_cows(self):
        secret = ['red', 'blue', 'green', 'yellow']
        guess = ['red', 'green', 'blue', 'yellow']
        self.assertEqual(compare_codes(secret, guess), (2, 2))

    def test_none_correct(self):
        secret = ['red', 'blue', 'green', 'yellow']
        guess = ['purple', 'black', 'purple', 'black']
        self.assertEqual(compare_codes(secret, guess), (0, 0))

if __name__ == '__main__':
    unittest.main()
