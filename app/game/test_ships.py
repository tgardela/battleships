import unittest

from ships import *

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


    def test_get_board(self):
        board = get_board()
        self.assertEqual(self.empty_board, board)


    def test_getting_ship_orientation(self):
        orientation = get_ship_orientation()

        self.assertTrue(orientation in ['vertical', 'horizontal'])


    def test_get_starting_point_vertical(self):
        ship_size = 3
        starting_point = get_starting_point(ship_size, 'vertical')
        max_ver = [x for x in range(1, 12 - ship_size)]
        max_hor = [x for x in range(1, 12)]

        self.assertTrue(starting_point[0] in  max_ver)
        self.assertTrue(starting_point[1] in  max_hor)


    def test_get_starting_point_horizontal(self):
        ship_size = 3
        starting_point = get_starting_point(ship_size, 'horizontal')
        max_ver = [x for x in range(1, 12)]
        max_hor = [x for x in range(1, 12 - ship_size)]

        self.assertTrue(starting_point[0] in  max_ver)
        self.assertTrue(starting_point[1] in  max_hor)


    def test_check_if_ship_can_be_put_near_boundary_should_be_negative(self):

        #left_top_corner
        left_top_vert = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (1, 1), 'vertical')
        left_top_hor = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (1, 1), 'horizontal')

        self.assertFalse(left_top_vert)
        self.assertFalse(left_top_hor)

        #top boundary
        top_ver =  check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (1, 5), 'vertical')
        top_hor =  check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (1, 5), 'horizontal')

        self.assertFalse(top_ver)
        self.assertFalse(top_hor)

        #right_top_corner
        right_top_vert = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (1, 10), 'vertical')
        right_top_hor = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (1, 8), 'horizontal')

        self.assertFalse(right_top_vert)
        self.assertFalse(right_top_hor)

        #right_boundary
        right_vert = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (4, 10), 'vertical')
        right_hor = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (4, 8), 'horizontal')

        self.assertFalse(right_vert)
        self.assertFalse(right_hor)

        #right_bottom_corner
        right_bottom_vert = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (8, 10), 'vertical')
        right_bottom_hor = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (10, 8), 'horizontal')

        self.assertFalse(right_bottom_vert)
        self.assertFalse(right_bottom_hor)

        #bottom_boundary
        bottom_vert = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (8, 6), 'vertical')
        bottom_hor = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (10, 5), 'horizontal')

        self.assertFalse(bottom_vert)
        self.assertFalse(bottom_hor)

        #left_bottom_corner
        left_bottom_vert = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (8, 1), 'vertical')
        left_bottom_hor = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (10, 1), 'horizontal')

        self.assertFalse(left_bottom_vert)
        self.assertFalse(left_bottom_hor)

        #left_boundary
        left_vert = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (4, 1), 'vertical')
        left_hor = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (4, 1), 'horizontal')

        self.assertFalse(left_vert)
        self.assertFalse(left_hor)


    def test_check_if_ship_can_be_put_near_boundary_should_be_positive(self):

        #left_top_corner
        left_top_vert = check_if_ship_can_be_put_there(self.empty_board, 3, (1, 1), 'vertical')
        left_top_hor = check_if_ship_can_be_put_there(self.empty_board, 3, (1, 1), 'horizontal')

        self.assertTrue(left_top_vert)
        self.assertTrue(left_top_hor)

        #top boundary
        top_ver =  check_if_ship_can_be_put_there(self.empty_board, 3, (1, 5), 'vertical')
        top_hor =  check_if_ship_can_be_put_there(self.empty_board, 3, (1, 5), 'horizontal')

        self.assertTrue(top_ver)
        self.assertTrue(top_hor)

        #right_top_corner
        right_top_vert = check_if_ship_can_be_put_there(self.empty_board, 3, (1, 10), 'vertical')
        right_top_hor = check_if_ship_can_be_put_there(self.empty_board, 3, (1, 8), 'horizontal')

        self.assertTrue(right_top_vert)
        self.assertTrue(right_top_hor)

        #right_boundary
        right_vert = check_if_ship_can_be_put_there(self.empty_board, 3, (4, 10), 'vertical')
        right_hor = check_if_ship_can_be_put_there(self.empty_board, 3, (4, 8), 'horizontal')

        self.assertTrue(right_vert)
        self.assertTrue(right_hor)

        #right_bottom_corner
        right_bottom_vert = check_if_ship_can_be_put_there(self.empty_board, 3, (8, 10), 'vertical')
        right_bottom_hor = check_if_ship_can_be_put_there(self.empty_board, 3, (10, 8), 'horizontal')

        self.assertTrue(right_bottom_vert)
        self.assertTrue(right_bottom_hor)

        #bottom_boundary
        bottom_vert = check_if_ship_can_be_put_there(self.empty_board, 3, (8, 6), 'vertical')
        bottom_hor = check_if_ship_can_be_put_there(self.empty_board, 3, (10, 5), 'horizontal')

        self.assertTrue(bottom_vert)
        self.assertTrue(bottom_hor)

        #left_bottom_corner
        left_bottom_vert = check_if_ship_can_be_put_there(self.empty_board, 3, (8, 1), 'vertical')
        left_bottom_hor = check_if_ship_can_be_put_there(self.empty_board, 3, (10, 1), 'horizontal')

        self.assertTrue(left_bottom_vert)
        self.assertTrue(left_bottom_hor)

        #left_boundary
        left_vert = check_if_ship_can_be_put_there(self.empty_board, 3, (4, 1), 'vertical')
        left_hor = check_if_ship_can_be_put_there(self.empty_board, 3, (4, 1), 'horizontal')

        self.assertTrue(left_vert)
        self.assertTrue(left_hor)


    def test_check_if_ship_can_be_put_in_the_middle_negative(self):
        middle_ver = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (4, 6), 'vertical')
        middle_hor = check_if_ship_can_be_put_there(self.board_with_ships_near_boundaries, 3, (4, 4), 'horizontal')

        self.assertFalse(middle_ver)
        self.assertFalse(middle_hor)


    def test_check_if_ship_can_be_put_in_the_middle_positive(self):
        middle_ver = check_if_ship_can_be_put_there(self.empty_board, 3, (4, 6), 'vertical')
        middle_hor = check_if_ship_can_be_put_there(self.empty_board, 3, (4, 4), 'horizontal')

        self.assertTrue(middle_ver)
        self.assertTrue(middle_hor)


    def test_put_ship_on_board(self):
        self.board_with_ship_coded = get_board()
        self.board_with_ship_coded[1][1] = 'P'
        board_with_ship = put_ship_on_board(self.empty_board, ship = 1, starting_point = (1,1), orientation = 'vertical')

        self.assertEqual(board_with_ship, self.board_with_ship_coded)


    def test_get_board_with_ships_placed_randomly(self):
        cells_used_by_five_ships = 82 #18 ship, one blank, 10 for cols, 10 for rows
        number_of_cells_used = sum(x.count('*') for x in get_board_with_ships_placed_randomly())

        self.assertEqual(cells_used_by_five_ships, number_of_cells_used)

if __name__=='__main__':
    unittest.main(verbosity=2)