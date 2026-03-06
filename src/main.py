from board import Board
from solver import solve


def main():

    regions = [
            [1,1,1,3,3,3,3,3,3],      #this board is an example, board will be given as an input
            [2,2,1,3,3,3,3,3,3],
            [2,2,1,3,3,3,4,4,4],
            [3,3,3,3,3,3,5,5,4],
            [3,6,6,7,3,3,5,5,5],
            [3,7,6,7,3,3,3,3,3],
            [3,7,7,7,8,8,9,3,3],
            [3,3,3,3,8,8,9,3,3],
            [3,3,3,3,9,9,9,3,3]
    ]

    board = Board(9, regions)

    if solve(board, 0):
        print("Solution found:\n")
        board.print_board()
    else:
        print("No solution")


if __name__ == "__main__":
    main()