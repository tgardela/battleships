from .ship import Ship


def get_board_with_ships_placed_randomly():
    board = get_board()
    ship_sizes = [5, 4, 3, 2, 2, 1, 1]
    for size in ship_sizes:
        name = get_ship_name(size)
        board = place_ship_on_board(board, size, name)
    return board


def get_board():
    board = [['*']*11 for i in range(11)]
    board[0][0] = ' '
    for b in range(1, 11):
        board[0][b] = str(b)
        board[b][0] = chr(64 + b)
    return board


def place_ship_on_board(board, size, name):
    ship = Ship(board, size, name)

    while not ship.can_be_put_there():
        ship.set_start_point()

    board = put_ship_on_board(board, ship)
    return board


def put_ship_on_board(board, ship):
    if ship.orientation == 'vertical':
        for i in range(ship.size):
            board[ship.start_point[0] + i][ship.start_point[1]] = ship.shipAbbreviation
    elif ship.orientation == 'horizontal':
        for i in range(ship.size):
            board[ship.start_point[0]][ship.start_point[1] + i] = ship.shipAbbreviation
    return board


def get_ship_name(size):
    ships = { 5 : 'an Aircraft Carrier',
              4 : 'a Battleship',
              3 : 'a Submarine',
              2 : 'a Destroyer',
              1 : 'a Patrol boat'}
    return ships[size]


def print_board(board):
    for row in board:
        print(' '.join(row))


def return_hit_ship_name(ship):
    ships = {'C' : 'an Aircraft Carrier',
             'B' : 'a Battleship',
             'S' : 'a Submarine',
             'D' : 'a Destroyer',
             'P' : 'a Patrol boat'}
    return ships[ship]


