from random import randint

from .validatedShip import ValidShip


def get_board_with_ships_placed_randomly():
    board = get_board()
    ships = [5, 4, 3, 2, 2, 1, 1]
    for ship in ships:
        orientation = get_ship_orientation()
        board = place_ship_on_board(board, ship, orientation)
    return board


def get_board():
    board = [['*']*11 for i in range(11)]
    board[0][0] = ' '
    for b in range(1, 11):
        board[0][b] = str(b)
        board[b][0] = chr(64 + b)
    return board


def get_ship_orientation():
    orientation =  randint(0,1)
    if orientation == 0:
        orientation = 'vertical'
    else:
        orientation = 'horizontal'
    return orientation


# def place_ship_on_board(board, ship, orientation):
#     starting_point = get_starting_point(ship, orientation)
#
#     while not check_if_ship_can_be_put_there(board, ship, starting_point, orientation):
#         starting_point = get_starting_point(ship, orientation)
#     board = put_ship_on_board(board, ship, starting_point, orientation)
#     return board

def place_ship_on_board(board, ship, orientation):
    starting_point = get_starting_point(ship, orientation)
    shipV = ValidShip(board, ship, starting_point, orientation)
    while not shipV.check_if_ship_can_be_put_there():
        print(ship, starting_point)
        print_board(board)
        starting_point = get_starting_point(ship, orientation)
<<<<<<< HEAD
        shipV = ValidShip(board, ship, starting_point, orientation)
=======
        
>>>>>>> bbbc66d47c3720b919b6dbf76428c46dbfd529c8
    board = put_ship_on_board(board, ship, starting_point, orientation)
    return board


def get_starting_point(ship, orientation):
    max_ver = 10
    max_hor = 10
    if orientation == 'vertical':
        max_ver = 10 - ship
    elif orientation == 'horizontal':
        max_hor = 10 - ship
    return randint(1, max_ver), randint(1, max_hor)


def check_if_ship_can_be_put_there(board, ship, start, orientation):
    start_row = start[0]
    start_col = start[1]

    if orientation == 'vertical':
        end_row = start_row + ship - 1
        col = start_col

        if col == 1:
            #left_top_corner
            if start_row == 1:
                for i in range(ship + 1):
                    if board[start_row + i][col] != '*' or board[start_row + i][col + 1] != '*':
                        return False
            #left_bottom_corner
            elif end_row == 10:
                for i in range(ship + 1):
                    if board[end_row - i][col] != '*' or board[end_row - i][col + 1] != '*':
                        return False
            #left_boundary
            else:
                for i in range(-1, ship + 1):
                    if board[start_row + i][col] != '*' or board[start_row + i][col + 1] != '*':
                        return False
        elif col == 10:
            #right_top_corner
            if start_row == 1:
                for i in range(ship + 1):
                    if board[start_row + i][col] != '*' or board[start_row + i][col - 1] != '*':
                        return False
            #right_bottom_corner
            elif end_row == 10:
                for i in range(ship + 1):
                    if board[end_row - i][col] != '*' or board[end_row - i][col - 1] != '*':
                        return False
            #right_boundary
            else:
                for i in range(-1, ship + 1):
                    if board[start_row + i][col - 1] != '*' or board[start_row + i][col] != '*':
                        return False
        else:
            #top_boundary
            if start_row == 1:
                for i in range(ship + 1):
                    if board[start_row + i][col - 1] != '*' or board[start_row + i][col] != '*' or board[start_row + i][col + 1] != '*':
                        return False
            #bottom_boundary
            elif end_row == 10:
                for i in range(ship + 1):
                    if board[end_row - i][col - 1] != '*' or board[end_row - i][col] != '*' or board[end_row - i][col + 1] != '*':
                        return False
            #not_near_any_boundary
            else:
                for i in range(-1, ship + 1):
                    if board[start_row + i][col - 1] != '*' or board[start_row + i][col] != '*' or board[start_row + i][col + 1] != '*':
                        return False
                if board[start_row - 1][col] != '*' or board[start_row + ship][col] != '*':
                    return False

    elif orientation == 'horizontal':
        end_col = start_col + ship - 1
        row = start_row

        if row == 1:
            #left_top_corner
            if start_col == 1:
                for i in range(ship + 1):
                    if board[row][start_col + i] != '*' or board[row + 1][start_col + 1] != '*':
                        return False
            #right_top_corner
            elif end_col == 10:
                for i in range(ship + 1):
                    if board[row][end_col - i] != '*' or board[row + 1][end_col - i] != '*':
                        return False
            #top_boundary
            else:
                for i in range(-1, ship + 1):
                    if board[row][start_col + i] != '*' or board[row + 1][start_col + i] != '*':
                        return False
        elif row == 10:
            #left_bottom_corner
            if start_col == 1:
                for i in range(ship + 1):
                    if board[row][start_col + i] != '*' or board[row - 1][start_col + i] != '*':
                        return False
            #right_bottom_corner
            elif end_col == 10:
                for i in range(ship + 1):
                    if board[row][end_col - i] != '*' or board[row - 1][end_col - i] != '*':
                        return False
            #bottom_boundary
            else:
                for i in range(-1, ship + 1):
                    if board[row - 1][start_col + i] != '*' or board[row][start_col + i] != '*':
                        return False
        else:
            #left_boundary
            if start_col == 1:
                for i in range(ship + 1):
                    if board[row - 1][start_col + i] != '*' or board[row][start_col + i] != '*' or board[row + 1][start_col + i] != '*':
                        return False
            #right_boundary
            elif end_col == 10:
                for i in range(ship + 1):
                    if board[row - 1][end_col - i] != '*' or board[row][end_col - i] != '*' or board[row + 1][end_col - i] != '*':
                        return False
            #not_near_any_boundary
            else:
                for i in range(-1, ship + 1):
                    if board[row - 1][start_col + i] != '*' or board[row][start_col + i] != '*' or board[row + 1][start_col + i] != '*':
                        return False
                if board[row][start_col - 1] != '*' or board[row][start_col + ship] != '*':
                    return False
    return True


def put_ship_on_board(board, ship, starting_point, orientation):
    ships = {5 : 'C', 4 : 'B', 3 : 'S', 2 : 'D', 1 : 'P'}
    
    if orientation == 'vertical':
        for i in range(ship):
            board[starting_point[0] + i][starting_point[1]] = ships[ship]
    elif orientation == 'horizontal':
        for i in range(ship):
            board[starting_point[0]][starting_point[1] + i] = ships[ship]
    return board


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
