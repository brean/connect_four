class FourConnect:
    def __init__(self, columns=7, rows=6, starting_player=1, players=None):
        self.starting_player = starting_player
        # we need at least a 4-by-4 map to play
        self.columns = max(4, columns)
        self.rows = max(4, rows)
        self.players = players if players else [1, 2]
        self.restart_game()

    def restart_game(self):
        """Restart the game, reset the board and set starting player"""
        self.board = [
            [0 for c in range(self.columns)]
            for r in range(self.rows)]
        self.win_cells = None  # cells that won the game, for debug
        self.current_player = self.starting_player

    def next_player(self):
        """Switch to the next player"""
        idx = self.players.index(self.current_player)
        if idx + 1 == len(self.players):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[idx + 1]

    def step(self, player, column):
        """Next step."""
        if player != self.current_player:
            # only the current player is allowed to make a move
            return
        if column >= len(self.board[0]):
            # ignore invalid columns
            return
        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = player
                self.next_player()
                return

    def won(self):
        """check the board if any of the players have won"""
        board = self.board
        rows = len(board)
        cols = len(board[0])
        if self.check_draw():
            return -1
        for player in self.players:
            # check horizontal
            for row in range(rows - 3):
                for col in range(cols):
                    cells = [(row + i, col) for i in range(4)]
                    if all([board[x][y] == player for x, y in cells]):
                        self.win_cells = cells
                        return player

            # check vertical
            for row in range(rows):
                for col in range(cols - 3):
                    cells = [(row, col + x) for x in range(4)]
                    if all([board[x][y] == player for x, y in cells]):
                        self.win_cells = cells
                        return player

            # check diagonal
            for row in range(rows - 3):
                for col in range(cols - 3):
                    cells = [(row + x, col + x) for x in range(4)]
                    if all([board[x][y] == player for x, y in cells]):
                        self.win_cells = cells
                        return player

            for row in range(rows - 3):
                for col in range(3, cols):
                    cells = [(row + x, col - x) for x in range(4)]
                    if all([board[x][y] == player for x, y in cells]):
                        self.win_cells = cells
                        return player

    def check_draw(self):
        return not any([
            self.board[r][c] == 0
            for r in range(self.rows)
            for c in range(self.columns)])

    def print_board(self, player1=1, player2=2, empty=0, border=True):
        """Return a string of the board that can be printed for debugging."""
        board_str = ''
        if border:
            board_str = f'+{"-" * len(self.board[0])}+'
        for y in range(len(self.board)):
            line = ''.join([
                str(self.board[y][x]) for x in range(len(self.board[y]))])
            if border:
                line = f'|{line}|'
            if board_str:
                board_str += '\n'
            board_str += line
        if border:
            board_str += f'\n+{"-" * len(self.board[0])}+'
        return board_str
