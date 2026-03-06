class Board:
    def __init__(self, size, regions):
        self.size = size
        self.regions = regions
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.grid:
            line = ""
            for cell in row:
                if cell == 1:
                    line += "Q "
                elif cell == -1:
                    line += "X "
                else:
                    line += ". "
            print(line)

    def place_queen(self, row, col):
        self.grid[row][col] = 1

    def remove_queen(self, row, col):
        self.grid[row][col] = 0

    def place_x(self, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = -1

    def region_has_queen(self, region_id):
        for r in range(self.size):
            for c in range(self.size):
                if self.regions[r][c] == region_id and self.grid[r][c] == 1:
                    return True
        return False

    def is_safe(self, row, col):
        # columna
        for r in range(self.size):
            if self.grid[r][col] == 1:
                return False

        # adyacentes
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r < 0 or c < 0 or r >= self.size or c >= self.size:
                    continue
                if self.grid[r][c] == 1:
                    return False

        # región
        region_id = self.regions[row][col]
        if self.region_has_queen(region_id):
            return False

        return True