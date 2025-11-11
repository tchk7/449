class Board:
    def __init__(self, size = 3):
        if size < 3 or size > 12:
            size = 3
        self._size = size
        self._grid = self._create_grid()

    def _create_grid(self):
        """Create an empty grid"""

        return [["" for _ in range(self._size)] for _ in range(self._size)]

    def is_empty(self, row, col):
        """Check if cell is empty"""
        return self._grid[row][col] == ""

    def is_full(self):
        """Check if board is full"""
        for row in range(self._size):
            for col in range(self._size):
                if self.is_empty(row, col):
                    return False
        return True

    def validate_move(self, row, col):
        """Check if a move is valid"""

        return (0 <= row < self._size and
                0 <= col < self._size and
                self.is_empty(row, col)
                )

    def put_letter(self, row, col, letter):
        """Place letter on board"""

        if self.validate_move(row, col):
            self._grid[row][col] = letter
            return True
        else:
            return False

    def get_cell(self, row, col):
        """Return cell value"""

        return self._grid[row][col]

    def reset_board(self):
        """Reset board to empty"""

        self._grid = self._create_grid()

    def get_size(self):
        """Return board size"""

        return self._size

    def get_empty_cells(self):
        """Return list of empty cells"""

        empty_cells = []

        for row in range(self._size):
            for col in range(self._size):
                if self.is_empty(row, col):
                    empty_cells.append([row, col])

        return empty_cells


