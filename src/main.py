from board import Board
from solver import solve


def main():

    regions = [
            [1,1,1,1,1,1,1,1],      #this board is an example, board will be given as an input
            [1,2,3,3,3,3,3,1],
            [1,2,3,3,3,3,4,1],
            [5,5,5,3,3,3,4,1],
            [6,5,3,3,3,4,4,4],
            [6,5,3,3,3,7,8,7],
            [6,6,6,6,7,7,8,7],
            [6,6,6,6,7,7,7,7]
    ]

    board = Board(8, regions)

    if solve(board, 0):
        print("Solution found:\n")
        board.print_board()
    else:
        print("No solution")


if __name__ == "__main__":
    main()