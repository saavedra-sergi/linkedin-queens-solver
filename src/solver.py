def solve(board, row=0):

    # Caso base: todas las filas completadas
    if row == board.size:
        return True

    # Probar todas las columnas en esta fila
    for col in range(board.size):

        if board.is_safe(row, col):
            # colocar reina
            board.place_queen(row, col)

            # intentar resolver siguiente fila
            if solve(board, row + 1):
                return True

            # backtrack: quitar reina
            board.remove_queen(row, col)
        #quiero ver cada fase del backtracking

        

    # ninguna posición válida encontrada en esta fila
    return False