import json
import sys
from board import Board
from solver import solve

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <puzzle_file.json>")
        return

    puzzle_file = sys.argv[1]

    with open(puzzle_file) as f:
        data = json.load(f)

    size = data["size"]
    regions = data["regions"]

    board = Board(size, regions)

    if solve(board):
        print("Solution found:\n")
        board.print_board()
    else:
        print("No solution")

if __name__ == "__main__":
    main()