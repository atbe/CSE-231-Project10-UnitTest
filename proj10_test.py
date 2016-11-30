import unittest
import proj10
import cards1
import cards
import pickle


class TestProj10(unittest.TestCase):
    """
    Tests for CSE 231 Project 10.

    Students must have used a main() function in order for this
    to work out smoothly. The program was originally interactive
    for input and it would intrude on the test process if we
    cannot prevent the main loop of the students' code before
    running our tests.

    An example to solutions for a problem like this can be found
    at the bottom of the proj10.py file provided as a sample
    with this test.


    Functions Tested:
        - setup_game
        -
    """

    def setUp(self):
        """
        Initialize a game.
        """
        # grab a game
        self._fnd, self._tab, self._stock, self._waste = proj10.setup_game()
        # grab a few cards
        self._heart_two_card = cards.Card(rank=2, suit=3)
        self._heart_three_card = cards.Card(rank=3, suit=3)
        self._club_two_card = cards.Card(rank=2, suit=1)
        self._club_three_card = cards.Card(rank=3, suit=1)
        # face down card
        self._face_down_card = cards.Card(rank=1, suit=3)
        if self._face_down_card.is_face_up():
            self._face_down_card.flip_card()


        # with open('enbody_game_elements.pckl', 'wb') as outfile:
            # (fnd, tab, stock, waste) = proj10.setup_game()
            # enbody_game_elements = {'tab': tab, 'fnd':fnd, 'stock': stock, 'waste': waste}
            # pickle.dump(enbody_game_elements, outfile)

        self._enbody_game_elements_dict = {} # temp
        try:
            with open('enbody_game_elements.pckl', 'rb') as infile:
                self._enbody_game_elements_dict = pickle.load(infile)
        except FileNotFoundError:
            raise FileNotFoundError('enbody_game_elements.pckl is required for this test.')

    def tearDown(self):
        """
        Teardown, nothing to do.
        """
        pass

    def testSetupGameFunction(self):
        """
        setup_game()


        Tests the setup_game function by checking all of its return values
        against the ouput from Dr.Enbody's solution.
        """

        # Check all of the elements to ensure the game was setup correctly.
        #
        # foundation
        self.assertListEqual(self._fnd, self._enbody_game_elements_dict['fnd'],
                msg='Foundation should be a list containing 4 empty lists initially.')
        # tableau
        self.assertListEqual(self._tab, self._enbody_game_elements_dict['tab'],
                msg='Tableau was not distributed in the correct manner. Check project PDF.\
                        Are you sure your project is using cards1.py?')
        # stock
        self.assertListEqual(self._stock, self._enbody_game_elements_dict['stock'],
                msg='Stock was not setup in the correct manner. Check the project PDF.\
                        Are you sure your project is using cards1.py?')
        # waste
        self.assertListEqual(self._waste, self._enbody_game_elements_dict['waste'],
                msg='Waste was not setup in the correct manner. Check t eh project PDF.\
                        Are you sure your project is using cards1.py?')

    def testValidFoundationMoveFunction(self):
        """
        valid_fnd_move(src_card : cards.Card, dest_Card : cards.Card)
        Returns:
            True - if move is valie bsed on requirenments below.

        Moving one card from foundation A(src_card) to foundation B(dest_card) requires that:
            - src_card and dest_card be face_up
            - src_card and dest_card have the SAME suit.
            - src_card.rank() is 1 greater than dest_card.rank()
                ~ src_card == 11, dest_card == 10, good.
            - if src_card is None, de
        """
        # test face down
        self.assertFalse(proj10.valid_fnd_move(self._face_down_card, self._heart_two_card),
                msg="A face down src_card is not a valid move.")
        self.assertFalse(proj10.valid_fnd_move(self._heart_two_card, self._face_down_card),
                msg="A face down dest_card is not a valid move.")

        # test diff suits
        self.assertFalse(proj10.valid_fnd_move(self._heart_two_card, self._club_two_card),
                msg="src_card msut have same suit as dest_card.")
        # test low src_card suits
        self.assertFalse(proj10.valid_fnd_move(self._heart_two_card, self._club_two_card),
                msg="src_card must have rank 2 higher than dest_card.")

        # test good input
        self.assertTrue(proj10.valid_fnd_move(self._heart_three_card, self._heart_two_card),
                msg="src_card with rank 1 higher than the dest_card and with same suit as dest_card is valid.")



if __name__ == '__main__':
    unittest.main()

