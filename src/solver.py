def solve_backtracking(board, row=0):

    # Caso base: todas las filas completadas
    if row == board.size:
        return True

    # Probar todas las columnas en esta fila
    for col in range(board.size):

        if board.is_safe(row, col):
            # colocar reina
            board.place_queen(row, col)

            # intentar resolver siguiente fila
            if solve_backtracking(board, row + 1):
                return True

            # backtrack: quitar reina
            board.remove_queen(row, col)
        
    # ninguna posición válida encontrada en esta fila
    return False


def solve_logic(board, row=0):
    #caso base
    if row == board.size:
        return True
        
    #recorrer la tabla
    for col in range(board.size):
        #we only evaluate if we're not in a cross
        if board.grid[row][col] != CROSS:
            #if it's a must, we put a queen and put crosses
            
            #must col
            if board.col_is_must(row, col, board.grid[row][col]):
                board.place_queen(row, col)
                board.place_queen_crosses(row, col)
            
            #must row
            if board.row_is_must(row, col, board.grid[row][col]):
                board.place_queen(row, col)
                board.place_queen_crosses(row, col)
            
            #must region
            




    return False