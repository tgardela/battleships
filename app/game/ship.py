from random import randint

from .ship_placement_validator import ShipPositionValidator

class Ship(object):
        
    def __init__(self, board, size, name):
        self.board = board
        self.size = size
        self.shipName = name
        self.orientation = None
        self.start_point = None
        self.shipAbbreviation = None

        self.set_orientation()
        self.set_start_point()
        self.set_ship_abbreviation()


    def set_orientation(self):
        random_orientation = randint(0, 1)
        if random_orientation == 0:
            self.orientation = 'vertical'
        else:
            self.orientation = 'horizontal'


    def set_start_point(self):
        max_ver = 10
        max_hor = 10
        if self.orientation == 'vertical':
            max_ver = 10 - self.size
        elif self.orientation == 'horizontal':
            max_hor = 10 - self.size
        self.start_point = (randint(1, max_ver), randint(1, max_hor))


    def can_be_put_there(self):
        ship_validator = ShipPositionValidator(self.board, self.size, self.start_point, self.orientation)
        return ship_validator.can_ship_be_put_there()


    def set_ship_abbreviation(self):
        abbreviations = {5: 'C', 4: 'B', 3: 'S', 2: 'D', 1: 'P'}
        self.shipAbbreviation = abbreviations[self.size]
