from four_connect import FourConnect

board = '''+-------+
|0000000|
|0000000|
|0000000|
|0000000|
|0000000|
|0000000|
+-------+'''


def test_print_board():
    fc = FourConnect()
    print(fc.print_board())
    assert fc.print_board() == board
