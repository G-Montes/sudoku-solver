import numpy

size = 9
region_size = int(numpy.sqrt(size))
#sudoku problem
#cells with value 0 are vacant cells
matrix1 = [
    [6, 5, 0, 8, 7, 3, 0, 9, 0],
    [0, 0, 3, 2, 5, 0, 0, 0, 8],
    [9, 8, 0, 1, 0, 4, 3, 5, 7],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 5, 0, 3],
    [5, 7, 8, 3, 0, 1, 0, 2, 6],
    [2, 0, 0, 0, 4, 8, 9, 0, 0],
    [0, 9, 0, 6, 2, 5, 0, 8, 1]]

matrix = [
    [5, 5, 0, 8, 7, 3, 0, 9, 0],
    [0, 0, 3, 2, 5, 0, 0, 0, 8],
    [9, 8, 0, 1, 0, 4, 3, 5, 7],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 5, 0, 3],
    [5, 7, 8, 3, 0, 1, 0, 2, 6],
    [2, 0, 0, 0, 4, 8, 9, 0, 0],
    [0, 9, 0, 6, 2, 5, 0, 8, 1]]

test = numpy.asarray(matrix1)

def print_board():
    for row in test:
        print(row)

def print_formatted_board():
    for i in range(size):
        if i % 3 == 0  and i != 0:
            print("---------------------")

        for j in range(size):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")
            if j == 8:
                print(test[i][j])
            else:
                print(test[i][j], end = " ")

def get_region(row, col):
    region_array = []
    row_start = (row // region_size) * region_size
    col_start = (col // region_size) * region_size

    for i in range(row_start, row_start + region_size):
        for j in range(col_start, col_start + region_size):
            region_array.append(test[i][j])
    
    return region_array

def check_board_validity():
    for i in range(0, size):
        row_no_zeroes = test[i, :][test[i, :] != 0]
        col_no_zeroes = test[:, i][test[:, i] != 0]

        if (numpy.unique(row_no_zeroes).size < row_no_zeroes.size or
            numpy.unique(col_no_zeroes).size < col_no_zeroes.size):
            return False

    for i in range(region_size):
        for j in range(region_size):
            region = numpy.asarray(get_region(i * region_size, j * region_size))
            region_no_zeroes = region[region != 0]

            if(numpy.unique(region_no_zeroes).size < region_no_zeroes.size):
                return False

    return True

#function to check if all cells are assigned or not
#if there is any unassigned cell
#then this function will change the values of
#row and col accordingly
def unsolved_cell():
    found_empty_cell = 0
    
    for i in range(0, size):
        for j in range(0, size):
            #cell is unassigned
            if test[i][j] == 0:
                row = i
                col = j
                found_empty_cell = 1
                cell_info = [row, col, found_empty_cell]
                return cell_info
    cell_info = [-1, -1, found_empty_cell]
    return cell_info

#function to check if we can put a
#value in a paticular cell or not
def number_is_valid(n, row, col):
    region = get_region(row, col)
    
    #checking in row
    if n in test[row, :]:
        return False

    #checking in column
    if n in test[:, col]:
        return False

    #checking submatrix
    if n in region:
        return False

    return True

#function to check if we can put a
#value in a paticular cell or not
def solve_sudoku():
    #if all cells are assigned then the sudoku is already solved
    #pass by reference because number_unassigned will change the values of row and col
    cell_info = unsolved_cell()
    if cell_info[2] == 0:
        return True
    row = cell_info[0]
    col = cell_info[1]
    #number between 1 to 9
    for i in range(1, size + 1):
        #if we can assign i to the cell or not
        #the cell is matrix[row][col]
        if number_is_valid(i, row, col):
            test[row][col] = i
            #backtracking
            if solve_sudoku():
                return True
            #if we can't proceed with this solution
            #reassign the cell
            test[row][col] = 0
    return False

# We want to make sure the board provided
# has valid values before proceeding
if not check_board_validity():
    print("Invalid board")
elif solve_sudoku():
    #Double check to make sure algorithm is working properly
    if check_board_validity(): 
        print_formatted_board()
    else:
        print("Unexpected error during solve. Result is not valid.")
else:
    print("No solution")
