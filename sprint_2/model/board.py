

class Board:
    def __init__(self, size = 3):
        if size < 3 or size > 12:
            size = 3
        self.size = size
        self.grid = self._create_grid()

    def _create_grid(self):
        """Create an empty grid"""

        return [["" for _ in range(self.size)] for _ in range(self.size)]

    def is_empty(self, row, col):
        """Check if cell is empty"""
        return self.grid[row][col] == ""

    def is_full(self):
        """Check if board is full"""
        for row in range(self.size):
            for col in range(self.size):
                if self.is_empty(row, col):
                    return False
        return True

    def validate_move(self, row, col):
        """Check if a move is valid"""

        return (0 <= row < self.size and
                0 <= col < self.size and
                self.is_empty(row, col)
                )

    def put_letter(self, row, col, letter):
        """Place letter on board"""

        if self.validate_move(row, col):
            self.grid[row][col] = letter
            return True
        else:
            return False

    def get_cell(self, row, col):
        """Return cell value"""

        return self.grid[row][col]

    def reset_board(self):
        """Reset board to empty"""

        self.grid = self._create_grid()



