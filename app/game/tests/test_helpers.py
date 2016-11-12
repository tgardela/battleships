import unittest
from flask import session

from app.game.helpers import *

class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.empty_board = get_empty_board()

        self.board_with_ships_near_boundaries = get_empty_board()
        self.board_with_ships_near_boundaries[5][5] = 'S'
        for i in range(1, 4):
            self.board_with_ships_near_boundaries[i + 1][2] = 'S'
            self.board_with_ships_near_boundaries[i + 1][9] = 'S'
            self.board_with_ships_near_boundaries[10- i][2] = 'S'
            self.board_with_ships_near_boundaries[10- i][9] = 'S'
            self.board_with_ships_near_boundaries[2][1 + i] = 'S'
            self.board_with_ships_near_boundaries[9][1 + i] = 'S'
            self.board_with_ships_near_boundaries[2][10 - i] = 'S'
            self.board_with_ships_near_boundaries[9][10 - i] = 'S'


    def test_mark_shot(self):
        pass


    def test_return_ship_name_from_cell_given(self):
        self.assertEqual('an Aircraft Carrier', return_ship_name_from_cell_given('C'))

if __name__=='__main__':
    unittest.main(verbosity=2)
