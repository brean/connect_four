from connect_four import ConnectFour


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
    cf = ConnectFour()
    assert game_states['empty'] == cf.board


def test_play_board():
    cf = ConnectFour()
    cf.step(1, 3)
    cf.step(2, 3)
    cf.step(1, 4)
    cf.step(2, 4)
    cf.step(1, 5)
    cf.step(2, 5)
    assert not cf.won()
    cf.step(1, 6)
    assert cf.won() == 1


def test_predefined_boards():
    cf = ConnectFour()
    for state in game_states:
        print(state)
        if state == 'empty':
            continue
        cf.board = game_states[state]
        assert cf.won() == 1
    cf.board = no_win
    assert not cf.won()


def test_draw():
    cf = ConnectFour()
    cf.board = draw
    assert cf.won() == -1
    cf.board[0][0] = 0
    cf.won()
    print(cf.win_cells)
    assert not cf.won()
