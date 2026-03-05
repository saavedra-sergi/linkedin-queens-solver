from board import Board


def main():
    size = 5
    board = Board(size)

    print("Initial board:")
    board.print_board()


if __name__ == "__main__":
    main()