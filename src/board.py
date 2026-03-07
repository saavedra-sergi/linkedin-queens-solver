QUEEN = -1
CROSS = -2

class Board:
    def __init__(self, size, regions):
        self.size = size
        self.regions = regions
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
    

    def print_board(self):
        for i in range(self.size):
            line = ""
            for j in range(self.size):
                if self.grid[i][j] == QUEEN:
                    line += "Q "
                else:
                    line += str(self.regions[i][j]) + " "
            print(line)


        #for row in self.grid:
           # line = ""
            #for cell in row:
             #   if cell == QUEEN:
              #      line += "Q "
               # elif cell == CROSS:
                #    line += "X "
                #else:
                 #   line += str(cell) + " "
            #print(line)

    def place_queen(self, row, col):
        self.grid[row][col] = QUEEN
        #when I place queen I put a cross in column, row and region:


    def remove_queen(self, row, col):
        self.grid[row][col] = 0
    
    def place_cross(self, row, col):
        self.grid[row][col] = CROSS
    
    

    def region_has_queen(self, region_id):
        for r in range(self.size):
            for c in range(self.size):
                if self.regions[r][c] == region_id and self.grid[r][c] == QUEEN:
                    return True
        return False
    
    def col_is_safe(self, col, n):
        # columna
        for r in range(self.size):
            if self.grid[r][col] == n:
                return False
        return True
    
    def row_is_safe(self, row, n):
        for c in range(self.size):
            if self.grid[row][c] == n:
                return False
        return True
     
    
    def adjacents_is_safe(self, row, col, n):
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r < 0 or c < 0 or r >= self.size or c >= self.size:
                    continue
                if self.grid[r][c] == n:
                    return False
        return True
    
    def region_is_safe(self, n):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == n:
                    return False
        return True
    

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
    
    def place_queen_crosses(self, row, col):
        #fill the entire row
        for r in range(self.size):
            if r != row:
                self.place_cross(row, col)
        
        #fill the entire col
        for c in range(self.size):
            if c != col:
                self.place_cross(row, col)
        
        #fill the adjacents
        self.place_cross(row + 1, col + 1)
        self.place_cross(row + 1, col + 1)
        self.place_cross(row - 1, col - 1)
        self.place_cross(row - 1, col - 1)
    

    def col_is_must(self, col):
        for r in range(self.size):
            counter = 0
            if self.grid[r][col] != CROSS:
                counter =+ 1
        if counter >=1:
            return False

        return True

    def row_is_must(self, row):
        for c in range(self.size):
            if self.grid[row][c] == CROSS:
                return False
        return True
    
    def region_is_must(self, n):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == n:
                    return False
        return True