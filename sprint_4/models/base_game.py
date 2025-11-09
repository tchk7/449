class BaseGame:
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.game_over = False

    def _is_valid(self ,row, col, size):

        valid_row = 0 <= row < size
        valid_col = 0 <= col < size

        return valid_row and valid_col


    def check_sos(self, row, col, letter):

        count = 0
        size = self.board.get_size()

        _all_dir = [(0, 1), (0, -1), (1, 0), (-1, 0),
                    (1, 1), (1, -1), (-1, 1), (-1, -1)]

        _o_dir = [(0, 1), (1, 0), (1, 1), (1, -1)]

        if letter == 'O':
            for row_pos, col_pos in _o_dir:
                row_1, col_1 = row + row_pos, col + col_pos
                row_2, col_2 = row - row_pos, col - col_pos

                if self._is_valid(row_1, col_1, size) and self._is_valid(row_2, col_2, size):
                    if self.board.get_cell(row_1, col_1) == 'S' and self.board.get_cell(row_2, col_2) == 'S':
                        count += 1

        elif letter == 'S':
            for row_pos, col_pos in _all_dir:
                o_row, o_col = row - row_pos, col - col_pos
                s_row, s_col = row - 2*row_pos, col - 2*col_pos

                if self._is_valid(o_row, o_col, size) and self._is_valid(s_row, s_col, size):
                    if self.board.get_cell(o_row, o_col) == 'O' and self.board.get_cell(s_row, s_col) == 'S':
                        count += 1

        return count

    def handle_move(self, row, col, player):
        return