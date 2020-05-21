import numpy

BOARD_SIZE = 9
REGION_SIZE = int(numpy.sqrt(BOARD_SIZE))
EMPTY = 0
INVALID_INDEX = -1
COLUMN = 0
ROW = 1
REGION = 2

def get_initial_sudoku_board(option):
    """
    Returns a list that contains the initial sudoku
    board state. The board returned depends on which
    option (an int) was passed in. 
    """
    return{
        1: [[6, 5, 0, 8, 7, 3, 0, 9, 0],
            [0, 0, 3, 2, 5, 0, 0, 0, 8],
            [9, 8, 0, 1, 0, 4, 3, 5, 7],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 5, 0, 3],
            [5, 7, 8, 3, 0, 1, 0, 2, 6],
            [2, 0, 0, 0, 4, 8, 9, 0, 0],
            [0, 9, 0, 6, 2, 5, 0, 8, 1]],

        2: [[6, 5, 0, 8, 7, 3, 0, 9, 0],
            [0, 6, 3, 2, 5, 0, 0, 0, 8],
            [9, 8, 0, 1, 0, 4, 3, 5, 7],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 5, 0, 3],
            [5, 7, 8, 3, 0, 1, 0, 2, 6],
            [2, 0, 0, 0, 4, 8, 9, 0, 0],
            [0, 9, 0, 6, 2, 5, 0, 8, 1]]
    }[option]
    
tested_sudoku_board = numpy.array(get_initial_sudoku_board(2))

def print_unformatted_board():
    """
    Prints the board. Every row is on its own line.
    """
    for row in tested_sudoku_board:
        print(row)


def print_formatted_board():
    """
    Prints a formatted board so that regions are 
    separated by a grid.
    """
    for i in range(BOARD_SIZE):
        if i % 3 == 0  and i != 0:
            print("---------------------")

        for j in range(BOARD_SIZE):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")
            if j == 8:
                print(tested_sudoku_board[i][j])
            else:
                print(tested_sudoku_board[i][j], end = " ")


def get_cell_region(row_index, col_index):
    """
    A cell's y,x index is passed in as an argument. This function
    determines what region the cell is in. Returns a list with all
    numbers in that region.
    """
    region_array = []

    region_row_start_index = (row_index // REGION_SIZE) * REGION_SIZE
    region_col_start_index = (col_index // REGION_SIZE) * REGION_SIZE

    region_row_end_index = region_row_start_index + REGION_SIZE
    region_col_end_index = region_col_start_index + REGION_SIZE

    for y in range(region_row_start_index, region_row_end_index):
        for x in range(region_col_start_index, region_col_end_index):
            region_array.append(tested_sudoku_board[y][x])
    
    return region_array


def get_valid_numbers_from_section(section):
    """
    Returns an array containing valid entries for the passed in section.
    A section can be either a row, column, or region.
    """
    return numpy.array([value for value in section 
                        if value != EMPTY])


def check_section_for_duplicates(section):
    """
    Returns True if the section contains no duplicate values. Returns false
    otherwise. Invalid entries are removed prior to checking for uniqueness.
    """
    valid_section_values = get_valid_numbers_from_section(section)
    unique_section_values = numpy.unique(valid_section_values)

    if unique_section_values.size < valid_section_values.size:
        return False
    return True

def check_board_for_duplicates():
    """
    Returns True if a board has no duplicate numbers for every row, 
    column, and region. Returns False otherwise. 
    """
    for index in range(0, BOARD_SIZE):
        # TODO Make a function that handles 0 removal
        row_without_zeroes = tested_sudoku_board[index, :][tested_sudoku_board[index, :] != 0]
        col_without_zeroes = tested_sudoku_board[:, index][tested_sudoku_board[:, index] != 0]
        # TODO Make a function that checks for uniquenes
        if (numpy.unique(row_without_zeroes).size < row_without_zeroes.size or
            numpy.unique(col_without_zeroes).size < col_without_zeroes.size):
            return False

    for region_row_index in range(REGION_SIZE):
        for region_col_index in range(REGION_SIZE):
            region = numpy.asarray(get_cell_region(region_row_index * REGION_SIZE, 
                                                   region_col_index * REGION_SIZE))
            region_no_zeroes = region[region != 0]

            if(numpy.unique(region_no_zeroes).size < region_no_zeroes.size):
                return False

    return True


def find_next_unsolved_cell():
    """
    Returns a tuple that contains the row and column index for
    the first cell encountered that contains and EMPTY value.
    Otherwise, it returns a tuple with INVALID_INDEX.  
    """
    for row_index in range(0, BOARD_SIZE):
        for col_index in range(0, BOARD_SIZE):
            #cell is unassigned
            if tested_sudoku_board[row_index][col_index] == EMPTY:
                return (row_index, col_index)
    
    return (INVALID_INDEX, INVALID_INDEX)


def number_is_valid(number_attempted, row_index, col_index):
    """
    Returns True if number is valid. False otherwise. Checks to see
    if number provided is already in the row, column, region that the 
    cell is in.
    """
    cell_region = get_cell_region(row_index, col_index)
    
    #checking in row
    if number_attempted in tested_sudoku_board[row_index, :]:
        return False

    #checking in column
    if number_attempted in tested_sudoku_board[:, col_index]:
        return False

    #checking submatrix
    if number_attempted in cell_region:
        return False

    return True


def solve_sudoku():
    """
    Returns True if a solution has been found, otherwise returns false.
    The function looks for the first empty cell it can find. Then it tries
    to assign a value to that cell if it's valid. It then moves on to the 
    next empty cell and repeats the process until no more empty cells are 
    left (in which case the board is assumed to be solved). If there's no 
    valid number for a particular cell, it goes back to the previous cell 
    assigned and tries a different number.  
    """
    cell_indexes = find_next_unsolved_cell()
    if cell_indexes[0] == INVALID_INDEX:
        return True
    
    row_index = cell_indexes[0]
    col_index = cell_indexes[1]
    
    for number_option in range(1, BOARD_SIZE + 1):
        if number_is_valid(number_option, row_index, col_index):
            tested_sudoku_board[row_index][col_index] = number_option
            # number_option has been successfully assigned so now
            # we try to assign a number in the next empty cell
            if solve_sudoku():
                return True
            # if this number_option doesn't lead to a solution,
            # reassign the cell to the default and try one of the
            # remaining options
            tested_sudoku_board[row_index][col_index] = EMPTY
    return False


# Make sure board provided doesn't have invalid numbers
if not check_board_for_duplicates():
    print("Invalid board")
elif solve_sudoku():
    #Double check to make sure algorithm is working properly
    if check_board_for_duplicates(): 
        print_formatted_board()
    else:
        print("Unexpected error during solve. Result is not valid.")
else:
    print("No solution")
