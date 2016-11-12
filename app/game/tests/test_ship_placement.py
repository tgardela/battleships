import unittest

from app.game.ship_placement import *


class TestShipPlacement(unittest.TestCase):
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


    def test_get_board_with_ships_placed_randomly(self):
        cells_used_by_five_ships = 82 #18 ship cells, one blank, 10 for cols, 10 for rows
        number_of_cells_used = sum(x.count('*') for x in get_board_with_ships_placed_randomly())

        self.assertEqual(cells_used_by_five_ships, number_of_cells_used)


    def test_get_empty_board(self):
        board = get_empty_board()

        self.assertEqual(self.empty_board, board)


    def test_get_board_with_ship_placed(self):
        board_with_ship = get_board_with_ship_placed(self.empty_board, size = 5, name = 'an Aircraft Carrier')

        self.assertEqual(6, sum(x.count('C') for x in board_with_ship)) # 6 because one 'C' is the row name


    def test_get_ship_name(self):
        self.assertEqual('an Aircraft Carrier', get_ship_name(5))


if __name__=='__main__':
    unittest.main(verbosity=2)