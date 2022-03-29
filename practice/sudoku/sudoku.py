from pprint import pprint

def find_next_empty(puzzle):
    # empty box is filled with -1
    # if there is no empty box return (None, None)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None

def is_valid(puzzle, guess, row, col):
    #figures out wether my guess is valid or not
    # checking in row, if the guess is already present then its invalid guess
    if guess in puzzle[row]:
        return False
    # checking in column, if the guess is already present then its invalid guess
    if guess in [puzzle[i][col] for i in range(9)]:
        return False
    #checking in the square box of 3x3
    #finding the 3x3 starts
    row_start = (row // 3)*3 # 1//3 =0, 5//3 =1, 7//3 =2
    col_start = (col // 3)*3 # 1//3 =0, 5//3 =1, 7//3 =2
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    # if all the above conditions is false then that means it is a valid guess, and we return true
    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking !
    # our puzzle is a list of lists, where each inner list is row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (is solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # if there is no empty box, then we are done
    if row is None:
        return True
    
    # step 2: if there is a place to put a guess, then we make a guess bet 1 and 9
    for guess in range(1, 10):
        # step 3: check if this guess or valid or not
        if is_valid(puzzle, guess, row, col):
            # step 3.3 if this is valid then place guess on the puzzle
            puzzle[row][col] = guess
            # now recursemusing this puzzle!
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid OR if our guess does not solve the sudoku, 
        # then we need to backtrack snd try a new number
        puzzle[row][col] = -1 # reset the guess

    # step 6: if nont of the guess works, then this puzzle is UNSOLVABLE
    return False            

if __name__=='__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)