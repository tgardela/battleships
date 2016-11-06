from random import randint


def get_shot():
    row = randint(1, 10)
    col = randint(1, 10)
    return row, col


def get_validated_shot(ships_to_sink):
    row, col = get_shot()
    chars = ['C', 'B', 'S', 'D', 'P', '*']
    while ships_to_sink[row][col] not in chars:
        row, col = get_shot()
    return row, col
