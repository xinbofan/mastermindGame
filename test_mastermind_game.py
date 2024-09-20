'''
    CS5001
    Final Project Test
    Xinbo Fan
'''

import unittest
from mastermind_game import Mastermindgame

class TestGuess(unittest.TestCase):
    '''
    Methods:
        test_check_bulls_and_cows_all_correct:
        Test the guess totally matches with the secret code
        test_check_bulls_and_cows_some_correct:
        Test the guess partially matches the secret code
    '''
    def test_check_bulls_and_cows_all_correct(self):
        '''
        Method -- test the guess totally matches with the secret code
        Parameters:
            self -- the current object
        '''
        game_1 = Mastermindgame()
        game_1.secret_code = ["red", "blue", "green", "yellow"]
        game_1.curr_guess = ["red", "blue", "green", "yellow"]
        result_1 = game_1.check_bulls_and_cows()
        self.assertEqual(result_1, [4, 0])

        game_2 = Mastermindgame()
        game_2.secret_code = ["black", "yellow", "green", "purple"]
        game_2.curr_guess = ["black", "yellow", "green", "purple"]
        result_2 = game_2.check_bulls_and_cows()
        self.assertEqual(result_2, [4, 0])

    def test_check_bulls_and_cows_some_correct(self):
        '''
        Method -- test the guess partially matches with the secret code
        Parameters:
            self -- the current object
        '''
        game_1 = Mastermindgame()
        game_1.secret_code = ["red", "blue", "green", "yellow"]
        game_1.curr_guess = ["purple", "blue", "green", "black"]
        result_1 = game_1.check_bulls_and_cows()
        self.assertEqual(result_1, [2, 0])

        game_2 = Mastermindgame()
        game_2.secret_code = ["black", "yellow", "green", "purple"]
        game_2.curr_guess = ["yellow", "black", "purple", "green"]
        result_2 = game_2.check_bulls_and_cows()
        self.assertEqual(result_2, [0, 4])

        game_3 = Mastermindgame()
        game_3.secret_code = ["black", "yellow", "green", "purple"]
        game_3.curr_guess = ["black", "green", "purple", "blue"]
        result_3 = game_3.check_bulls_and_cows()
        self.assertEqual(result_3, [1, 2])

if __name__ == '__main__':
    unittest.main()
