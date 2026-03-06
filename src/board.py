QUEEN = -1

class Board:
    def __init__(self, size, regions):
        self.size = size
        self.regions = regions
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
    

    def print_board(self):
        for row in self.grid:
            line = ""
            for cell in row:
                if cell == QUEEN:
                    line += "Q "
                else:
                    line += str(cell) + " "
            print(line)

    def place_queen(self, row, col):
        self.grid[row][col] = QUEEN

    def remove_queen(self, row, col):
        self.grid[row][col] = 0
    

    def region_has_queen(self, region_id):
        for r in range(self.size):
            for c in range(self.size):
                if self.regions[r][c] == region_id and self.grid[r][c] == QUEEN:
                    return True
        return False
    
    

    def is_safe(self, row, col):
        # columna
        for r in range(self.size):
            if self.grid[r][col] == QUEEN:
                return False

        # adyacentes
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r < 0 or c < 0 or r >= self.size or c >= self.size:
                    continue
                if self.grid[r][c] == QUEEN:
                    return False

        # región
        region_id = self.regions[row][col]
        if self.region_has_queen(region_id):
            return False

        return True