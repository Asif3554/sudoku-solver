import random

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:  # Look for empty cells
                return r, c
    return None, None

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if 'num' is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:  # If no empty cell, puzzle is solved
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, row, col, guess):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = -1  # Backtrack

    return False

def fill_sudoku(board):
    # Attempt to fill the board with random numbers
    for row in range(9):
        for col in range(9):
            if board[row][col] == -1:  # Look for an empty cell
                numbers = list(range(1, 10))
                random.shuffle(numbers)  # Shuffle to randomize the filling
                for num in numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if fill_sudoku(board):
                            return True
                        board[row][col] = -1  # Backtrack if needed
                return False  # If no number is valid, backtrack
    return True

def remove_numbers(board, num_to_remove=40):
    # Remove `num_to_remove` numbers randomly to create a puzzle
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)
    for _ in range(num_to_remove):
        row, col = positions.pop()
        board[row][col] = -1

def generate_sudoku_board():
    board = [[-1] * 9 for _ in range(9)]  # Initialize an empty board
    fill_sudoku(board)  # Fill the board with a valid Sudoku solution
    remove_numbers(board)  # Remove some numbers to create a puzzle
    return board

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != -1 else '.' for num in row))

# Generate and print a randomized Sudoku board
sudoku_board = generate_sudoku_board()
print("Randomized Sudoku Puzzle:")
print_board(sudoku_board)

# Solve the puzzle
if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("\nCould not solve the Sudoku board.")
