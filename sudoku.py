# example puzzles:
test_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

test_puzzle2 = [
    [4, 0, 6, 5, 0, 2, 8, 0, 9],
    [0, 0, 0, 0, 4, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
    [6, 0, 0, 8, 0, 0, 1, 0, 0],
    [5, 0, 0, 0, 7, 0, 0, 8, 0],
    [3, 0, 2, 9, 0, 4, 0, 6, 0],
    [0, 2, 0, 6, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 5, 3, 9, 4, 0],
    [8, 3, 0, 0, 9, 0, 0, 0, 2]
]

# solver(puzzle) solves the sudoku puzzle
def solver(puzzle):
    if not empty_slot(puzzle):
        return True
    else:
        row_pos = empty_slot(puzzle)[0]
        column_pos = empty_slot(puzzle)[1]

    for possible_num in range(1, 10):
        if valid_num(puzzle, possible_num, row_pos, column_pos):
            puzzle[row_pos][column_pos] = possible_num

            if solver(puzzle):
                 return puzzle

            else:
                puzzle[row_pos][column_pos] = 0

    return False

# empty_slot(puzzle) returns False if the puzzle is completed, and otherwise returns the position of an empty space in
# in the puzzle
def empty_slot(puzzle):
    for row in range(0, 9):
        for column in range(0, 9):
            if puzzle[row][column] == 0:
                return [row, column]
    return False

# valid_num(puzzle, num, row_pos, column_pos) returns False if the provided [num] is not a valid value for that position
# of the puzzle and returns True otherwise
def valid_num(puzzle, num, row_pos, column_pos):
    # checking the row
    for i in range(0, 9):
        if puzzle[row_pos][i] == num:
            return False
    # checking the column
    for i in range(0, 9):
        if puzzle[i][column_pos] == num:
            return False
    # checking the 3 x 3 "square"
    for i in range(0, 3):
        for j in range(3):
            if puzzle[(row_pos // 3) * 3 + i][(column_pos // 3) * 3 + j] == num:
                return False
    return True

