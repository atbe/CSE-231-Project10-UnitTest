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

    """
    Helper functions
    """
    def grab_test_tab_col(self, length=1):
        """
        Returns:
           Tableau column default initialized with desired length.

        Choose a length 1 - 7 inclusive
        """
        if not (1 <= length and length <= 7):
            raise ValueError("1 - 7 tab length required for grab_test_tab_col.")

        return self._tab[length - 1][:]

    def setUp(self):
        """
        Initialize a game.
        """
        # re-route cards to cards1
        cards = cards1

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

    """
    Tests
    """

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
                msg='Stock was not setup in the correct manner.\nSize = {}.\nCheck the project PDF.\
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
                msg='Waste was not setup in the correct manner.\nSize = {}\nIt should have one card Check t eh project PDF.\
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
        self.assertFalse(proj10.valid_fnd_move(self._heart_three_card, self._club_two_card),
                msg="src_card must have same suit as dest_card.")
        # test low src_card rank
        self.assertFalse(proj10.valid_fnd_move(self._heart_two_card, self._heart_two_card),
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
        self.assertFalse(proj10.valid_tab_move(self._heart_two_card, self._heart_three_card),
                msg="src_card must have different suit than dest_card.")
        # test low dest_card rank
        self.assertFalse(proj10.valid_tab_move(self._heart_three_card, self._club_two_card),
                msg="src_card must have rank 2 higher than dest_card.")

        # test good input
        self.assertTrue(proj10.valid_tab_move(self._heart_two_card, self._club_three_card),
                msg="dest_card with rank 1 higher than the src_card and with diff suit than dest_card is valid input.")

# tableau_to_foundation empty test

    def testTableauToFoundationEmptyPushBad(self):
        """
        tableau_to_foundation(tab_col : list, fnd_col : list)
        Returns:
            None

        This test ensures pushing a card != ace to an empty fnd fails.
        """

        # test empty foundation
        with self.assertRaises(RuntimeError, msg="Empty foundation should throw error when passing a card that is not an ace."):
            # 2 of clubs
            test_card = cards.Card(rank=2, suit=1)
            test_tab = self.grab_test_tab_col(1)
            test_tab.append(test_card)
            proj10.tableau_to_foundation(test_tab, [])

    def testTableauToFoundationEmptyPushGood(self):
        """
        tableau_to_foundation(tab_col : list, fnd_col : list)
        Returns:
            None

        This test ensures pushing an ace to an empty fnd succeeds.
        """
        # test adding ace to empty foundation
        #
        # ace of clubs
        test_card = cards.Card(rank=1, suit=1)
        test_tab = self.grab_test_tab_col(1)
        test_tab.append(test_card)
        test_fnd = []
        proj10.tableau_to_foundation(test_tab, test_fnd)
        self.assertEqual(test_card, test_fnd[-1],
                msg="Pushing ace to an empty fnd should work fine.")


# tableau_to_foundation rank test

    def testTableauToFoundationRankBad(self):
        """
        tableau_to_foundation(tab_col : list, fnd_col : list)
        Returns:
            None

        Good suit, bad rank.
        """
        with self.assertRaises(RuntimeError, msg="Pushing a card to fnd requires it to the cards \
rank to be no more than 1 greater than the dest_card."):
            # test source tableau
            test_tab_col_src = [cards.Card(rank=3, suit=1)]
            # test destination foundation with an ace on top
            test_fnd_col_dest = [cards.Card(rank=1, suit=1)]
            proj10.tableau_to_foundation(test_tab_col_src, test_fnd_col_dest)

# tableau_to_foundation suit test

    def testTableauToFoundationSuitGoodRankGood(self):
        """
        tableau_to_foundation(tab_col : list, fnd_col : list)
        Returns:
            None

        Good suit, good rank.
        """
        # test source tableau
        test_src_card = cards.Card(rank=2, suit=1)
        test_tab_col_src = [test_src_card]
        # test destination foundation with an ace on top
        test_fnd_col_dest = [cards.Card(rank=1, suit=1)]
        proj10.tableau_to_foundation(test_tab_col_src, test_fnd_col_dest)
        self.assertTrue(test_fnd_col_dest[-1] == test_src_card,
                msg="tab_to_fnd should succed if tab[-1] is same suit as dest.")


    def testTableauToFoundationSuitBad(self):
        """
        tableau_to_foundation(tab_col : list, fnd_col : list)
        Returns:
            None

        Bad suit, good rank.
        """
        with self.assertRaises(RuntimeError, msg="Pushing a card to fnd requires it to the cards have same suit."):
            # test source tableau
            test_tab_col_src = [cards.Card(rank=2, suit=2)]
            # test destination foundation with an ace on top
            test_fnd_col_dest = [cards.Card(rank=1, suit=1)]
            proj10.tableau_to_foundation(test_tab_col_src, test_fnd_col_dest)


# tableau_to_foundation face test

    def testTableauToFoundationFaceGood(self):
        """
        tableau_to_foundation(tab_col : list, fnd_col : list)
        Returns:
            None

        Good suit, good rank, face up.
        """
        # test source tableau
        test_src_card = cards.Card(rank=2, suit=1)
        if not test_src_card.is_face_up():
            test_src_card.flip_card()
        test_tab_col_src = [test_src_card]
        # test destination foundation with an ace on top
        test_fnd_col_dest = [cards.Card(rank=1, suit=1)]
        proj10.tableau_to_foundation(test_tab_col_src, test_fnd_col_dest)
        self.assertTrue(test_fnd_col_dest[-1] == test_src_card,
                msg="tab_to_fnd should succeed if tab[-1] is face up.")

    def testTableauToFoundationFaceBad(self):
        """
        tableau_to_foundation(tab_col : list, fnd_col : list)
        Returns:
            None

        Bad suit, good rank.
        """
        with self.assertRaises(RuntimeError, msg="Pushing a card to fnd requires it to the src_card be face up."):
            test_src_card = cards.Card(rank=2, suit=1)
            if test_src_card.is_face_up():
                test_src_card.flip_card()
            # test source tableau
            test_tab_col_src = [test_src_card]
            # test destination foundation with an ace on top
            test_fnd_col_dest = [cards.Card(rank=1, suit=1)]
            proj10.tableau_to_foundation(test_tab_col_src, test_fnd_col_dest)

# tableau_to_foundation last card in tableau face up

    def testTableauToFoundationFlipLastTabCard(self):
        """
        tableau_to_foundation(tab_col : list, fnd_col : list)
        Returns:
            None

        Card at the bottom of the source tab_col should be flipped up.
        """
        test_tab_col = self.grab_test_tab_col(2)
        # flip the last card and push something that is a valid move
        test_tab_col[-1].flip_card()
        test_tab_col.append(cards.Card(rank=2, suit=1))
        test_fnd = [cards.Card(rank=1, suit=1)]
        proj10.tableau_to_foundation(test_tab_col, test_fnd)
        self.assertTrue(test_tab_col[-1].is_face_up(),
                msg="Card at the bottom of a tableau cannot be face down after valid tab_to_fnd move.")

# waste_to_foundation rank test

    def testWasteToFoundationRankBad(self):
        """
        waste_to_foundation(waste : list, fnd_col : list)
        Returns:
            None

        Good suit, bad rank.
        """
        with self.assertRaises(RuntimeError, msg="Pushing a card to fnd requires it to the cards \
rank to be 1 higher than what is on the top of the fnd."):
            # test source waste
            test_waste_src = [cards.Card(rank=3, suit=1)]
            # test destination foundation with an ace on top
            test_fnd_col_dest = [cards.Card(rank=1, suit=1)]
            try:
                proj10.waste_to_foundation(test_waste_src, test_fnd_col_dest)
            except TypeError as e:
                # print("Dr. Enbody may have caused some students to add/not add the source parameter to this method. We try both.", str(e))
                proj10.waste_to_foundation(test_waste_src, test_fnd_col_dest, [])

# waste_to_foundation suit test

    def testWasteToFoundationSuitBad(self):
        """
        waste_to_foundation(waste : list, fnd_col : list)
        Returns:
            None

        Bad suit, good rank.
        """
        with self.assertRaises(RuntimeError, msg="Pushing a card to fnd requires it to the cards have same suits."):
            # test source waste
            test_waste_src = [cards.Card(rank=2, suit=2)]
            # test destination foundation with an ace on top
            test_fnd_col_dest = [cards.Card(rank=1, suit=1)]
            try:
                proj10.waste_to_foundation(test_waste_src, test_fnd_col_dest)
            except TypeError as e:
                proj10.waste_to_foundation(test_waste_src, test_fnd_col_dest, [])

    def testWasteToFoundationRankGoodSuitGood(self):
        """
        waste_to_foundation(waste : list, fnd_col : list, stock : Deck)
        Returns:
            None

        Good suit, good rank.
        """
        # test source tableau
        test_src_card = cards.Card(rank=2, suit=1)
        test_src_waste = [test_src_card]
        # test destination foundation with an ace on top
        test_fnd_col_dest = [cards.Card(rank=1, suit=1)]
        #
        try:
            proj10.waste_to_foundation(test_src_waste, test_fnd_col_dest)
        except TypeError as e:
            proj10.waste_to_foundation(test_src_waste, test_fnd_col_dest, [])

        self.assertTrue(test_fnd_col_dest[-1] == test_src_card,
                msg="tab_to_fnd should succed if tab[-1] is 1 rank higher than dest.")

# waste_to_foundation empty test

    def testWasteToFoundationEmptyBad(self):
        """
        waste_to_foundation(waste : list, fnd_col : list, stock : Deck)
        Returns:
            None

        Empty waste should throw a runtime error
        """
        with self.assertRaises(RuntimeError, msg="If waste is empty, exception should be thrown when used."):
            # test waste
            test_waste = []
            # test destination foundation with an ace on top
            test_fnd_col_dest = [cards.Card(rank=1, suit=1)]
            proj10.tableau_to_foundation(test_waste, test_fnd_col_dest)

# waste_to_tableau rank/suit tests

    def testWasteToTableauRankBad(self):
        """
        waste_to_tableau(waste : list, tab_col : list, stock : Deck)
        Returns:
            None

        Good suit, bad rank.
        """
        with self.assertRaises(RuntimeError, msg="Pushing a card to fnd that is not one rank lower\
than the rank of what is on the top of the fnd is an error."):
            # test source waste
            test_waste_src = [cards.Card(rank=1, suit=2)]
            # test destination foundation with an ace on top
            test_tab_col_dest = [cards.Card(rank=3, suit=1)]
            try:
                proj10.waste_to_tableau(test_waste_src, test_tab_col_dest)
            except TypeError as e:
                proj10.waste_to_tableau(test_waste_src, test_tab_col_dest, [])

    def testWasteToTableauSuitBad(self):
        """
        waste_to_tableau(waste : list, tab_col : list, stock : Deck)
        Returns:
            None

        Bad suit, bad rank.
        """
        with self.assertRaises(RuntimeError, msg="Pushing a card to tab with same suit as tab[-1] is an error."):
            # test source waste
            test_waste_src = [cards.Card(rank=1, suit=1)]
            # test destination foundation with an ace on top
            test_tab_col_dest = [cards.Card(rank=2, suit=1)]
            try:
                proj10.waste_to_tableau(test_waste_src, test_tab_col_dest)
            except TypeError as e:
                proj10.waste_to_tableau(test_waste_src, test_tab_col_dest, [])

    def testWasteToTableauRankGoodSuiteGood(self):
        """
        waste_to_tableau(waste : list, tab_col : list, stock : Deck)
        Returns:
            None

        Good suit, good rank.
        """
        # test source tableau
        test_src_card = cards.Card(rank=1, suit=1)
        test_src_waste = [test_src_card]
        # test destination foundation with an ace on top
        test_tab_col_dest = [cards.Card(rank=2, suit=2)]
        #
        try:
            proj10.waste_to_tableau(test_src_waste, test_tab_col_dest)
        except TypeError as e:
            proj10.waste_to_tableau(test_src_waste, test_tab_col_dest, [])

        self.assertTrue(test_tab_col_dest[-1] == test_src_card,
                msg="tab_to_fnd should succed if tab[-1] is 1 rank higher than dest and suits are diff")


# waste_to_tableau face test

    def testWasteToTableauFaceDown(self):
        """
        waste_to_tableau(waste : list, tab_col : list, stock : Deck)
        Returns:
            None

        Good suit, good rank.
        """
        with self.assertRaises(RuntimeError, msg="Face down source card should cause an error."):
            # test source waste
            test_waste_src = [cards.Card(rank=1, suit=2)]
            if test_waste_src[-1].is_face_up():
                test_waste_src[-1].flip_card()

            # test destination foundation with an ace on top
            test_tab_col_dest = [cards.Card(rank=2, suit=1)]
            try:
                proj10.waste_to_tableau(test_waste_src, test_tab_col_dest)
            except TypeError as e:
                proj10.waste_to_tableau(test_waste_src, test_tab_col_dest, [])

    def testWasteToTableauFaceUp(self):
        """
        waste_to_tableau(waste : list, tab_col : list, stock : Deck)
        Returns:
            None

        Good suit, good rank.
        """
        # test source tableau
        test_src_card = cards.Card(rank=1, suit=1)
        if not test_src_card.is_face_up():
            test_src_card.flip_card()
        test_src_waste = [test_src_card]
        # test destination foundation with an ace on top
        test_tab_col_dest = [cards.Card(rank=2, suit=2)]
        #
        try:
            proj10.waste_to_tableau(test_src_waste, test_tab_col_dest)
        except TypeError as e:
            proj10.waste_to_tableau(test_src_waste, test_tab_col_dest, [])

        self.assertTrue(test_tab_col_dest[-1] == test_src_card,
                msg="tab_to_fnd should succed if source card is face up and valid.")

    def teststockToWasteEmptyStockBad(self):
        """
        stock_to_waste(stock : Deck, waste : list<Card>)
        Returns:
            None

        Empty stock.
        """
        with self.assertRaises(RuntimeError, msg="RuntimeError should be thrown when moving from stock to waste and stock is empty."):
            empty_stock = cards.Deck()
            empty_stock._Deck__deck = []
            waste = []
            proj10.stock_to_waste(empty_stock, waste)

    def teststockToWasteEmptyStockGood(self):
        """
        stock_to_waste(stock : Deck, waste : list<Card>)
        Returns:
            None

        Non-empty stock.
        """
        non_empty_stock = cards.Deck()
        sample_card = non_empty_stock._Deck__deck[-1]
        waste = []
        proj10.stock_to_waste(non_empty_stock, waste)
        self.assertTrue(waste[-1] == sample_card,
                msg="Non-Empty stock should move a card to the top of the tableau.")




if __name__ == '__main__':
    unittest.main()

