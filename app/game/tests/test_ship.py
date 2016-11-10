import unittest

from app.game.ship import Ship
from app.game.ship_placement import get_board


class TestShipPlacement(unittest.TestCase):
    def setUp(self):
        self.empty_board = get_board()
        self.ship = Ship(self.empty_board, size=5, name='an Aircraft Carrier')

        self.full_board = get_board()
        for i in range(1, 11):
            for j in range(1, 11):
                self.full_board[i][j] = 'S'

    def test_getting_ship_orientation(self):
        self.assertTrue(self.ship.orientation in ['vertical', 'horizontal'])


    def test_get_starting_point_vertical(self):
        if self.ship.orientation == 'vertical':
            max_ver = [x for x in range(1, 12 - self.ship.size)]
            max_hor = [x for x in range(1, 12)]

            self.assertTrue(self.ship.start_point[0] in  max_ver)
            self.assertTrue(self.ship.start_point[1] in  max_hor)
        else:
            max_ver = [x for x in range(1, 12)]
            max_hor = [x for x in range(1, 12 - self.ship.size)]

            self.assertTrue(self.ship.start_point[0] in max_ver)
            self.assertTrue(self.ship.start_point[1] in max_hor)


    def test_set_ship_abbreviation(self):
        self.assertEqual('C', self.ship.shipAbbreviation)


    def test_can_be_put_there_true(self):
        self.assertEqual(True, self.ship.can_be_put_there())


    def test_can_be_put_there_false(self):
        ship = Ship(self.full_board, size=5, name='an Aircraft Carrier')

        self.assertEqual(False, ship.can_be_put_there())


if __name__=='__main__':
    unittest.main(verbosity=2)