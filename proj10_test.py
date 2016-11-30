import unittest
import proj10
import cards1


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

    def test_setup_game(self):
        pass

if __name__ == '__main__':
    unittest.main()
