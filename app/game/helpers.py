from flask import request, session

from .ship_placement import get_empty_board, get_board_with_ships_placed_randomly


def set_oceans_and_ships(number_of_players):
    session['first_shots'] = get_empty_board()
    session['first_ships'] = get_board_with_ships_placed_randomly()
    session['second_ships'] = get_board_with_ships_placed_randomly()

    if number_of_players == 2:
        session['second_shots'] = get_empty_board()
        session['first_msg'] = ''
        session['second_msg'] = ''


def get_player_shot():
    return int(request.form['row']), int(request.form['col'])


def mark_shot(board, ships_to_sink, row, col):
    cell = ships_to_sink[row][col]
    if cell == '*':
        board[row][col] = 'O'
        ships_to_sink[row][col] = 'O'
        msg ='missed'
    elif cell in ['C', 'B', 'S', 'D', 'P']:
        board[row][col] = 'X'
        ships_to_sink[row][col] = 'X'
        msg = 'hit %s' % return_ship_name_from_cell_given(cell)
    else:
        msg = 'already shot there'
    return board, msg


def return_ship_name_from_cell_given(ship):
    ships = {'C' : 'an Aircraft Carrier',
             'B' : 'a Battleship',
             'S' : 'a Submarine',
             'D' : 'a Destroyer',
             'P' : 'a Patrol boat'}
    return ships[ship]
