from four_connect import FourConnect


game_states = {
    'empty': [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ],
    'one_won_horizontal': [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0],
        [0, 0, 2, 2, 0, 0, 0]
    ],
    'one_won_vertical': [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 2, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0]
    ],
    'one_won_diagonal1': [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 2, 1, 0, 0, 0, 0],
        [0, 2, 2, 1, 0, 0, 0],
        [0, 2, 1, 2, 1, 0, 0]
    ],
    'one_won_diagonal2': [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 2, 0, 0],
        [0, 0, 1, 2, 2, 0, 0],
        [0, 1, 2, 1, 2, 0, 0]
    ],
    'one_won_border': [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 2, 1],
        [0, 0, 0, 0, 0, 2, 1],
        [0, 0, 0, 0, 0, 2, 1]
    ]
}

no_win = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 2, 0, 0, 1],
    [0, 1, 2, 1, 2, 0, 1],
    [0, 1, 2, 1, 1, 1, 2]
]

draw = [
    [1, 2, 2, 1, 2, 1, 2],
    [2, 1, 1, 2, 1, 2, 2],
    [1, 1, 1, 2, 1, 1, 1],
    [2, 2, 1, 2, 1, 1, 2],
    [1, 1, 2, 1, 2, 2, 1],
    [2, 1, 2, 1, 2, 2, 2]
]


def test_empty_board():
    fc = FourConnect()
    assert game_states['empty'] == fc.board


def test_play_board():
    fc = FourConnect()
    fc.step(1, 3)
    fc.step(2, 3)
    fc.step(1, 4)
    fc.step(2, 4)
    fc.step(1, 5)
    fc.step(2, 5)
    assert not fc.won()
    fc.step(1, 6)
    assert fc.won() == 1


def test_predefined_boards():
    fc = FourConnect()
    for state in game_states:
        print(state)
        if state == 'empty':
            continue
        fc.board = game_states[state]
        assert fc.won() == 1
    fc.board = no_win
    assert not fc.won()


def test_draw():
    fc = FourConnect()
    fc.board = draw
    assert fc.won() == -1
    fc.board[0][0] = 0
    fc.won()
    print(fc.win_cells)
    assert not fc.won()
