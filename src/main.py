from board import Board
from solver import solve


def main():

    size = 7
    board = Board(size)

    solved = solve(board, 0)

    if solved:
        print("Solution found:\n")
        board.print_board()
    else:
        print("No solution found")


if __name__ == "__main__":
    main()