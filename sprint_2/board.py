

class Board:
    def __init__(self, size = 3):
        if size < 3:
            size = 3
        self.size = size
        self._create_grid()

    def _create_grid(self):
        """Create an empty grid"""
        self.grid = []

        for rowIndex in range(self.size):
            row = []
            for colIndex in range(self.size):
                row.append("")
            self.grid.append(row)

    def is_empty(self, row, col):
        """Check if cell is empty"""
        return self.grid[row][col] == ""

    def is_full(self):
        """Check if board is full"""
        for rowIndex in range(self.size):
            for colIndex in range(self.size):
                if self.is_empty(rowIndex, colIndex):
                    return False
        return True

    def put_letter(self, row, col, letter):
        """Place letter on board"""

        if self.is_empty(row, col):
            self.grid[row][col] = letter
            return True
        else:
            return False

    def get_cell(self, row, col):
        """Return cell value"""

        if self.is_empty(row, col):
            return ""
        else:
            return self.grid[row][col]




