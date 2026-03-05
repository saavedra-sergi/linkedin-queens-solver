def solve(board, row):

    # caso base: todas las filas completadas
    if row == board.size:
        return True

    # probar todas las columnas
    for col in range(board.size):

        if board.is_safe(row, col):

            board.place_queen(row, col)

            # intentar resolver la siguiente fila
            if solve(board, row + 1):
                return True

            # backtrack
            board.remove_queen(row, col)

    return False