class Board:

    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.grid:
            line = ""
            for cell in row:
                if cell == 1:
                    line += "Q "
                else:
                    line += ". "
            print(line)