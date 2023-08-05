from four_connect import FourConnect


game_states = [
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1]
    ]

]


def test_play_game():
    fc = FourConnect()
    assert fc.board == game_states[0]
    fc.step(1, 3)
    assert fc.board == game_states[1]
    # ignore illegal turns (same player again)
    fc.step(1, 3)
    assert fc.board == game_states[1]
    fc.step(2, 3)
    assert fc.board == game_states[2]
    fc.step(1, 2)
    assert fc.board == game_states[3]
    fc.step(2, 3)
    assert fc.board == game_states[4]
    # ignore out-of-board
    fc.step(1, 8)
    assert fc.board == game_states[4]
    fc.step(1, 6)
    assert fc.board == game_states[5]
