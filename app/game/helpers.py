from flask import request, session

from .ships import get_board, get_board_with_ships_placed_randomly, return_hit_ship_name


def set_oceans_and_ships(number_of_players):
    session['first_shots'] = get_board()
    session['second_ships'] = get_board_with_ships_placed_randomly()

    if number_of_players == 2:
        session['second_shots'] = get_board()
        session['first_msg'] = ''
        session['second_msg'] = ''
    session['first_ships'] = get_board_with_ships_placed_randomly()


def get_player_shot():
    return int(request.form['row']), int(request.form['col'])


def mark_shot(board, ships_to_sink, row, col):
    cell = ships_to_sink[row][col]
    if cell == '*':
        board[row][col] = 'O'
        msg ='missed'
    elif cell in ['C', 'B', 'S', 'D', 'P']:
        board[row][col] = 'X'
        msg = 'hit %s' % return_hit_ship_name(cell)
    else:
        msg = 'already shot there'
    return board, msg