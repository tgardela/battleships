import unittest

from app.game.ship_placement_validator import ShipPositionValidator
from app.game.ship_placement import get_empty_board

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


    def test_can_ship_be_put_left_top_corner_false(self):
        shipValidatorVert = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (1, 1), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (1, 1), 'horizontal')

        self.assertFalse(shipValidatorVert.can_ship_be_put_there())
        self.assertFalse(shipValidatorHor.can_ship_be_put_there())

    def test_can_ship_be_put_top_boundary_false(self):
        shipValidatorVert = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (1, 5), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (1, 5), 'horizontal')

        self.assertFalse(shipValidatorVert.can_ship_be_put_there())
        self.assertFalse(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_right_top_corner_false(self):
        shipValidatorVert = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (1, 10), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (1, 8), 'horizontal')

        self.assertFalse(shipValidatorVert.can_ship_be_put_there())
        self.assertFalse(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_right_boundary_false(self):
        shipValidatorVert = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (4, 10), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (4, 8), 'horizontal')

        self.assertFalse(shipValidatorVert.can_ship_be_put_there())
        self.assertFalse(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_right_bottom_corner_false(self):
        shipValidatorVert = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (8, 10), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (10, 8), 'horizontal')

        self.assertFalse(shipValidatorVert.can_ship_be_put_there())
        self.assertFalse(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_bottom_boundary_false(self):
        shipValidatorVert = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (8, 6), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (10, 5), 'horizontal')

        self.assertFalse(shipValidatorVert.can_ship_be_put_there())
        self.assertFalse(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_left_bottom_corner_false(self):
        shipValidatorVert = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (8, 1), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (10, 1), 'horizontal')

        self.assertFalse(shipValidatorVert.can_ship_be_put_there())
        self.assertFalse(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_left_boundary_false(self):
        shipValidatorVert = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (4, 1), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (4, 1), 'horizontal')

        self.assertFalse(shipValidatorVert.can_ship_be_put_there())
        self.assertFalse(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_left_top_corner_true(self):
        shipValidatorVert = ShipPositionValidator(self.empty_board, 3, (1, 1), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.empty_board, 3, (1, 1), 'horizontal')

        self.assertTrue(shipValidatorVert.can_ship_be_put_there())
        self.assertTrue(shipValidatorHor.can_ship_be_put_there())

    def test_can_ship_be_put_top_boundary_true(self):
        shipValidatorVert = ShipPositionValidator(self.empty_board, 3, (1, 5), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.empty_board, 3, (1, 5), 'horizontal')

        self.assertTrue(shipValidatorVert.can_ship_be_put_there())
        self.assertTrue(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_right_top_corner_true(self):
        shipValidatorVert = ShipPositionValidator(self.empty_board, 3, (1, 10), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.empty_board, 3, (1, 8), 'horizontal')

        self.assertTrue(shipValidatorVert.can_ship_be_put_there())
        self.assertTrue(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_right_boundary_true(self):
        shipValidatorVert = ShipPositionValidator(self.empty_board, 3, (4, 10), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.empty_board, 3, (4, 8), 'horizontal')

        self.assertTrue(shipValidatorVert.can_ship_be_put_there())
        self.assertTrue(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_right_bottom_corner_true(self):
        shipValidatorVert = ShipPositionValidator(self.empty_board, 3, (8, 10), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.empty_board, 3, (10, 8), 'horizontal')

        self.assertTrue(shipValidatorVert.can_ship_be_put_there())
        self.assertTrue(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_bottom_boundary_true(self):
        shipValidatorVert = ShipPositionValidator(self.empty_board, 3, (8, 6), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.empty_board, 3, (10, 5), 'horizontal')

        self.assertTrue(shipValidatorVert.can_ship_be_put_there())
        self.assertTrue(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_left_bottom_corner_true(self):
        shipValidatorVert = ShipPositionValidator(self.empty_board, 3, (8, 1), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.empty_board, 3, (10, 1), 'horizontal')

        self.assertTrue(shipValidatorVert.can_ship_be_put_there())
        self.assertTrue(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_left_boundary_true(self):
        shipValidatorVert = ShipPositionValidator(self.empty_board, 3, (4, 1), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.empty_board, 3, (4, 1), 'horizontal')

        self.assertTrue(shipValidatorVert.can_ship_be_put_there())
        self.assertTrue(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_in_the_middle_false(self):
        shipValidatorVert = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (4, 6), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.board_with_ships_near_boundaries, 3, (4, 4), 'horizontal')

        self.assertFalse(shipValidatorVert.can_ship_be_put_there())
        self.assertFalse(shipValidatorHor.can_ship_be_put_there())


    def test_can_ship_be_put_in_the_middle_true(self):
        shipValidatorVert = ShipPositionValidator(self.empty_board, 3, (4, 6), 'vertical')
        shipValidatorHor = ShipPositionValidator(self.empty_board, 3, (4, 4), 'horizontal')

        self.assertTrue(shipValidatorVert.can_ship_be_put_there())
        self.assertTrue(shipValidatorHor.can_ship_be_put_there())


if __name__=='__main__':
    unittest.main(verbosity=2)