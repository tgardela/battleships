from flask import render_template, request, session, url_for, redirect

from .app import app
from .game.aiplayer import get_validated_shot
from .game.helpers import get_player_shot, mark_shot, set_oceans_and_ships


@app.route('/')
@app.route('/index/')
def index():
    session.clear()
    return render_template('index.html')


@app.route('/single/', methods=['GET', 'POST'])
def single():
    if session.get('first_shots') is None:
        set_oceans_and_ships(number_of_players = 1)

    if request.method == 'GET':
        return render_template('single_first.html', first_shots=session['first_shots'], first_ships=session['first_ships'],
                               second_ships=session['second_ships'])

    if request.method == 'POST':
        row, col = get_player_shot()
        session['first_shots'], first_msg = mark_shot(session['first_shots'], session['second_ships'], row, col)

        ai_row, ai_col = get_validated_shot(session['first_ships'])
        session['first_ships'], second_msg = mark_shot(session['first_ships'], session['first_ships'], ai_row, ai_col)

        if sum(x.count('X') for x in session['first_shots']) == 18:
            winner = 'You'
            return render_template('endgame.html', winner=winner)
        elif sum(x.count('X') for x in session['first_ships']) == 18:
            winner = 'AI'
            return render_template('endgame.html', winner=winner)

        return render_template('single_first.html', first_shots=session['first_shots'], first_ships=session['first_ships'],
                                second_ships=session['second_ships'], first_msg=first_msg, second_msg=second_msg)


@app.route('/first/', methods=['GET', 'POST'])
def first():
    if session.get('first_shots') is None:
        set_oceans_and_ships(number_of_players = 2)

    if request.method == 'GET':
        return render_template('single_first.html', first_shots=session['first_shots'], first_ships=session['first_ships'],
                               second_ships=session['second_ships'], first_msg=session['first_msg'],
                                second_msg= session['second_msg'])

    if request.method == 'POST':
        row, col = get_player_shot()
        session['first_shots'], session['first_msg'] = mark_shot(session['first_shots'], session['second_ships'], row, col)
        session['second_ships'], _ = mark_shot(session['second_ships'], session['second_ships'], row, col)

        if sum(x.count('X') for x in session['first_shots']) == 18:
            winner='Player One'
            return render_template('endgame.html', winner=winner)

        return redirect(url_for('second', second_shots=session['second_shots'], second_ships=session['second_ships'],
                                first_ships=session['first_ships'], first_msg=session['first_msg'],
                                second_msg= session['second_msg']))


@app.route('/second/', methods=['GET', 'POST'])
def second():
    if request.method == 'GET':
        return render_template('second.html', second_shots=session['second_shots'], second_ships=session['second_ships'],
                               first_ships=session['first_ships'], first_msg=session['first_msg'],
                                second_msg= session['second_msg'])

    if request.method == 'POST':
        row, col = get_player_shot()
        session['second_shots'], session['second_msg'] = mark_shot(session['second_shots'], session['first_ships'], row, col)
        session['first_ships'], _ = mark_shot(session['first_ships'], session['first_ships'], row, col)

        if sum(x.count('X') for x in session['second_shots']) == 18:
            winner='Player Two'
            return render_template('endgame.html', winner=winner)

        return redirect(url_for('first', first_shots=session['first_shots'], first_ships=session['first_ships'],
                                second_ships=session['second_ships'], second_msg=session['second_msg'],
                                first_msg=session['first_msg']))


@app.route('/endgame/')
def endgame():
    return render_template('endgame.html')

