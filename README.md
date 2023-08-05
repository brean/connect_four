# four_connect
Four connect logic to use in any other project.

# Installation
You can use pip to install:

```bash
$ pip install four_connect
```

# Usage
To create a new game simple create a new instance of the `FourConnect`-class.
You can also configure the size of your game, the starting player and the
number of player. The default is a 7*6 board with 2 players where player "1"
starts:

```python
import four_connect
fc = four_connect.FourConnect(columns=7, rows=6, starting_player=1)
```

You can then call `fc.step(...)` to play the next piece, it gets the player and the column as parameter. A game could look like this:

```python
fc.step(1, 3)
fc.step(2, 3)
fc.step(1, 4)
fc.step(2, 4)
fc.step(1, 4)
```

You need to check if one of the players won manually after each step:
```python
>>> import four_connect
>>> fc = four_connect.FourConnect(columns=7, rows=6, starting_player=1)
>>> fc.step(1, 3)
>>> fc.step(2, 3)
>>> fc.step(1, 4)
>>> fc.step(2, 4)
>>> fc.step(1, 5)
>>> fc.step(2, 5)
>>> fc.won()
None
>>> fc.step(1, 6)
>>> fc.won()
1
```
If a player won it returns the players number, while the game is undecided it 
returns `None`.

If all tiles are played (there are no free spots left) the game is called a draw and the `won` function returns `-1`.

For debugging you can always print the current board:
```python
>>> print(fc.print_board())
# +-------+
# |0000000|
# |0000000|
# |0000000|
# |0000100|
# |0002200|
# |0001100|
# +-------+
```

To start a new game (empty the board and reset the starting player) call
`fc.restart_game()`.