from connect_four import ConnectFour

board = '''+-------+
|0000000|
|0000000|
|0000000|
|0000000|
|0000000|
|0000000|
+-------+'''


def test_print_board():
    cf = ConnectFour()
    print(cf.print_board())
    assert cf.print_board() == board
