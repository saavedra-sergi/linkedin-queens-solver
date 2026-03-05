from board import Board


def main():

    board = Board(5)

    if board.is_safe(0, 2):
        board.place_queen(0, 2)

    if board.is_safe(2, 2):
        board.place_queen(2, 2)
    else:
        board.place_X(2,2)

    board.print_board()


if __name__ == "__main__":
    main()