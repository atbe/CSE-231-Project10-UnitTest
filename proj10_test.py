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
        self._fnd, self._tab, self._stock, self._waste = proj10.setup_game()

        # with open('enbody_game_elements.pckl', 'wb') as outfile:
            # (fnd, tab, stock, waste) = proj10.setup_game()
            # enbody_game_elements = {'tab': tab, 'fnd':fnd, 'stock': stock, 'waste': waste}
            # pickle.dump(enbody_game_elements, outfile)

        enbody_game_elements = {} # temp
        try:
            with open('enbody_game_elements.pckl', 'rb') as infile:
                enbody_game_elements = pickle.load(infile)
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
        self.assertListEqual(self._fnd, enbody_game_elements['fnd'],
                msg='Foundation should be a list containing 4 empty lists initially.')
        # tableau
        self.assertListEqual(self._tab, enbody_game_elements['tab'],
                msg='Tableau was not distributed in the correct manner. Check project PDF.\
                        Are you sure your project is using cards1.py?')
        # stock
        self.assertListEqual(self._stock, enbody_game_elements['stock'],
                msg='Stock was not setup in the correct manner. Check the project PDF.\
                        Are you sure your project is using cards1.py?')
        # waste
        self.assertListEqual(self._waste, enbody_game_elements['waste'],
                msg='Waste was not setup in the correct manner. Check t eh project PDF.\
                        Are you sure your project is using cards1.py?')

if __name__ == '__main__':
    unittest.main()

