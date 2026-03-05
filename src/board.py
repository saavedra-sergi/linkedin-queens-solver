class Board:
    #empty -> 0
    #queens ->1
    #cross -> 2



    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.grid:
            line = ""
            for cell in row:
                if cell == 1:
                    line += "Q "
                if cell == 2:
                    line += "X "
                if cell == 0:
                    line += ". "
            print(line)
    
    def place_queen(self, row, col):
        self.grid[row][col] = 1
    
    def place_X(self, row, col):
        self.grid[row][col] = 2

    def remove_queen(self, row, col):
        self.grid[row][col] = 0

    
    def is_safe(self, row, col):

        # comprobar columna
        for r in range(self.size):
            if self.grid[r][col] == 1:
                return False

        # comprobar casillas adyacentes
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):

                if r < 0 or c < 0 or r >= self.size or c >= self.size:
                    continue

                if self.grid[r][c] == 1:
                    return False

        return True