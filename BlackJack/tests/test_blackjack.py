from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_with_user_busting(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand greater than 21, while dealer ends up with hand less than 21.
        The dealer wins with user BUSTING.
        '''
        output = run_test([10, 5, 10], ['y'], [10, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n"  \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 7\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_with_blackjack(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand less than 21, while dealer ends up with hand 21.
        The dealer wins with a BLACKJACK.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [10, 5, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_with_both_bust(self, input_mock, randint_mock):
        '''
        Both dealer and user recives hand value greater than 21.
        The dealer wins as per the game rules.
        '''
        output = run_test([9, 9, 9], ['y'], [10, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a 10\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_with_greater_hand(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [5, 10, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Dealer has 15.\n" \
                   "Drew a 4\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_with_blackjack(self, input_mock, randint_mock):
        '''
        Dealer gets a hand that is less than 21 while user gets 21.
        The user wins with Blackjack.
        '''
        output = run_test([5, 5, 8, 3], ['y', 'y'], [5, 10, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Dealer has 15.\n" \
                   "Drew a 4\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_with_greater_hand(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output = run_test([10, 5, 3], ['y','n'], [10, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 7\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_with_dealerbust(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand less than 21, while dealer ends up with hand greater than 21.
        The user wins with dealer getting busted.
        '''
        output = run_test([10, 5, 3], ['y','n'], [8, 7, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 7\n" \
                   "Dealer has 15.\n" \
                   "Drew a 10\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_draw_with_both_blackjack(self, input_mock, randint_mock):
        '''
        Both dealer and user recives hand value of 21.
        The game is tied.
        '''
        output = run_test([3, 5, 8, 5], ['y', 'y'], [10, 5, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_draw_with_both_getting_same_hand(self, input_mock, randint_mock):
        '''
        Both dealer and user recives same hand value which is less than 21.
        The game is tied.
        '''
        output = run_test([5, 5, 9], ['y', 'n'], [10, 5, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 5\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a 4\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_draw_with_both_standing(self, input_mock, randint_mock):
        '''
        Both dealer and user recives same hand value which is less than 21.
        The game is tied.
        '''
        output = run_test([9, 9], ['n'], [10, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an 8\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    
    

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
