import unittest

from app.game.ship_placement_validator import ShipPositionValidator
from app.game.ship_placement import get_board, get_board_with_ships_placed_randomly, place_ship_on_board, print_board, put_ship_on_board

class TestShipPlacement(unittest.TestCase):
    def setUp(self):
        self.empty_board = get_board() 

        self.board_with_ships_near_boundaries = get_board()
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
        cells_used_by_five_ships = 82 #18 ship, one blank, 10 for cols, 10 for rows
        number_of_cells_used = sum(x.count('*') for x in get_board_with_ships_placed_randomly())

        self.assertEqual(cells_used_by_five_ships, number_of_cells_used)


    def test_get_board(self):
        board = get_board()

        self.assertEqual(self.empty_board, board)


    def test_put_ship_on_board(self):
        board_with_ship = place_ship_on_board(self.empty_board, size = 1, name = 'a Patrol boat')

        self.assertEqual(1, sum(x.count('P') for x in board_with_ship))


    # def test_put_ship_on_board(self):
    #     board1 =  place_ship_on_board(self.empty_board, size = 1, name = 'a Patrol boat')
    #     board2 = put_ship_on_board(self.empty_board, ship = 1)
    #     print_board(board1)
    #     print_board(board2)


if __name__=='__main__':
    unittest.main(verbosity=2)