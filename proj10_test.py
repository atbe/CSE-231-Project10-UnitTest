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

    An example to a solution for a problem like this can be found
    at the bottom of the proj10.py file provided as a sample
    with this test. It uses the global __name__ variable.
    This way, we can import the module to use the functions like
    we have for this test, and run the proj10.py alone for regular
    output.


    Functions Tested:
        - setup_game
        - valid_fnd_move
        - valid_tab_move
    """

    def setUp(self):
        """
        Initialize a game.
        """
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
                enbody_game_elements_dict = pickle.load(infile)
                self._fnd = enbody_game_elements_dict['fnd']
                self._tab = enbody_game_elements_dict['tab']
                self._waste = enbody_game_elements_dict['waste']
                self._stock = enbody_game_elements_dict['stock']
        except FileNotFoundError:
            raise FileNotFoundError('enbody_game_elements.pckl is required for this test.')

    def tearDown(self):
        """
        Teardown, nothing to do.
        """
        pass

    def testSetupGameFunctionTableau(self):
        """
        setup_game() -> tableau


        Testing tableau from setup_game.
        """

        # grab a test game
        fnd, tab, stock, waste = proj10.setup_game()

        # tableau
        self.assertListEqual(tab, self._tab,
                msg='Tableau was not distributed in the correct manner. Check project PDF.\
                        Are you sure your project is using cards1.py?')

    def testSetupGameFunctionStock(self):
        """
        setup_game() -> stock


        Testing stock from setup_game.
        """

        # grab a test game
        fnd, tab, stock, waste = proj10.setup_game()

        # stock
        self.assertListEqual(stock, self._stock,
                msg='Stock was not setup in the correct manner.\nSize = {}. Check the project PDF.\
                        Are you sure your project is using cards1.py?'.format(len(stock)))

    def testSetupGameFunctionWaste(self):
        """
        setup_game() -> waste


        Testing waste from setup_game.
        """

        # grab a test game
        fnd, tab, stock, waste = proj10.setup_game()

        # waste
        self.assertListEqual(waste, self._waste,
                msg='Waste was not setup in the correct manner.\nSize = {} It should have one card Check t eh project PDF.\
                        Are you sure your project is using cards1.py?'.format(len(waste)))

    # not used for project scoring
    '''
    def testSetupGameFunction(self):
        """
        setup_game() -> tableau


        Tests the setup_game function by checking all of its return values
        against the ouput from Dr.Enbody's solution.
        """

        # grab a test game
        fnd, tab, stock, waste = proj10.setup_game()

        # Check all of the elements to ensure the game was setup correctly.
        #
        # foundation
        self.assertListEqual(fnd, self._fnd,
                msg='Foundation should be a list containing 4 empty lists initially.')
        # tableau
        self.assertListEqual(tab, self._tab,
                msg='Tableau was not distributed in the correct manner. Check project PDF.\
                        Are you sure your project is using cards1.py?')
        # stock
        self.assertListEqual(stock, self._stock,
                msg='Stock was not setup in the correct manner. Check the project PDF.\
                        Are you sure your project is using cards1.py?')
        # waste
        self.assertListEqual(waste, self._waste,
                msg='Waste was not setup in the correct manner. It should have one card Check t eh project PDF.\
                        Are you sure your project is using cards1.py?')
    '''

    def testValidFoundationMoveFunction(self):
        """
        valid_fnd_move(src_card : cards.Card, dest_Card : cards.Card)
        Returns:
            True - if move is valid based on requirements below.

        Moving one card to a foundation must satisfy these conditions.
            - src_card and dest_card be face_up
            - src_card and dest_card have the SAME suit.
            - src_card.rank() is 1 greater than dest_card.rank()
                ~ src_card == 11, dest_card == 10, good.
        """
        # test face down
        self.assertFalse(proj10.valid_fnd_move(self._face_down_card, self._heart_two_card),
                msg="A face down src_card is not a valid move.")
        self.assertFalse(proj10.valid_fnd_move(self._heart_two_card, self._face_down_card),
                msg="A face down dest_card is not a valid move.")

        # test diff suits
        self.assertFalse(proj10.valid_fnd_move(self._heart_two_card, self._club_two_card),
                msg="src_card must have same suit as dest_card.")
        # test low src_card rank
        self.assertFalse(proj10.valid_fnd_move(self._heart_two_card, self._club_two_card),
                msg="src_card must have rank 2 higher than dest_card.")

        # test good input
        self.assertTrue(proj10.valid_fnd_move(self._heart_three_card, self._heart_two_card),
                msg="src_card with rank 1 higher than the dest_card and with same suit as dest_card is valid input.")


    def testValidTableauMoveFunction(self):
        """
        valid_tab_move(src_card : cards.Card, dest_Card : cards.Card)
        Returns:
            True - if move is valid based on requirements below.

        Moving one card to a tabluea must satisfy these conditions
            - src_card and dest_card be face_up
            - src_card and dest_card have the DIFF suit.
            - src_card.rank() is 1 less than dest_card.rank()
                ~ src_card == 10, dest_card == 11, good.
        """
        # test face down
        self.assertFalse(proj10.valid_tab_move(self._face_down_card, self._heart_two_card),
                msg="A face down src_card is not a valid move.")
        self.assertFalse(proj10.valid_tab_move(self._heart_two_card, self._face_down_card),
                msg="A face down dest_card is not a valid move.")

        # test same suits
        self.assertFalse(proj10.valid_fnd_move(self._heart_two_card, self._heart_two_card),
                msg="src_card must have different suit than dest_card.")
        # test low dest_card rank
        self.assertFalse(proj10.valid_fnd_move(self._heart_three_card, self._club_two_card),
                msg="src_card must have rank 2 higher than dest_card.")

        # test good input
        self.assertTrue(proj10.valid_fnd_move(self._heart_three_card, self._heart_two_card),
                msg="dest_card with rank 1 higher than the src_card and with diff suit than dest_card is valid input.")


    def testTableauToFoundation(self):
        """
        tableau_to_foundation(tab_col : list, fnd_col : list)
        Returns:
            None

        Pre-Conditions:

        """
        # test a non-ace card to empty foundation
        with self.assertRaises(RuntimeError):
            # 2 of clubs
            test_card = cards.Card(2, 1)
            test_fnd = self._fnd[0][:]
            test_tab = self._tab[0][:]
            test_tab.append(test_card)
            proj10.tableau_to_foundation(test_tab, test_fnd)
        # with 






if __name__ == '__main__':
    unittest.main()

