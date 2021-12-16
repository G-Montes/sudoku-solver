import cv2 as cv
import pytesseract as pt
import numpy as np

# Loading Image
sudoku_img_path = r"C:\\Users/genar/Documents/431.jpg"
sudoku_img_path2 = r"C:\\Users/genar/Documents/sudoku_easy_001_solution.jpg"
sudoku_img_path3 = r"C:\\Users/genar/Documents/src.png"


sudoku_img = cv.imread(sudoku_img_path3, 0)
cv.imshow("", sudoku_img)
cv.waitKey(0)
#Acquire Cell boundaries
numRows, numColumns = sudoku_img.shape
sudokuSize = 9
sudokuCellSize = numRows // 9
sudoku_board = np.zeros(sudokuSize * sudokuSize, dtype=int)

invert_img = cv.bitwise_not(sudoku_img)
invert_img = cv.adaptiveThreshold(invert_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

horizontal = np.copy(invert_img)
vertical = np.copy(invert_img)

# Horizontal Edges

horizontal_struct = cv.getStructuringElement(cv.MORPH_RECT, (sudokuCellSize, 1))
horizontal = cv.erode(horizontal, horizontal_struct)
horizontal = cv.dilate(horizontal, horizontal_struct, iterations=2)
horizontal_struct = cv.getStructuringElement(cv.MORPH_RECT, (sudokuCellSize, 2))
horizontal = cv.dilate(horizontal, horizontal_struct, iterations=4)

(rows, cols) = np.where(horizontal != 0)
sudoku_img[rows, cols] = horizontal[rows, cols]

# Vertical Edges
vertical_struct = cv.getStructuringElement(cv.MORPH_RECT, (1, sudokuCellSize))
vertical = cv.erode(vertical, vertical_struct)
vertical = cv.dilate(vertical, vertical_struct, iterations=2)
vertical_struct = cv.getStructuringElement(cv.MORPH_RECT, (2, sudokuCellSize))
vertical = cv.dilate(vertical, vertical_struct, iterations=4)

(rows, cols) = np.where(vertical != 0)
sudoku_img[rows, cols] = vertical[rows, cols]

# Other stuff
removed_grid_board = cv.threshold(sudoku_img, 200, 255, cv.THRESH_BINARY)
sudoku_img = removed_grid_board[1]

large_sudoku_img = cv.resize(sudoku_img, (0, 0), fx= 3, fy= 3, interpolation = cv.INTER_NEAREST)


num_struct = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))
large_sudoku_img = cv.dilate(large_sudoku_img, num_struct)

large_sudoku_img = cv.medianBlur(large_sudoku_img, 3)

large_num_rows, large_num_columns = large_sudoku_img.shape
large_sudoku_cell_size = large_num_rows // 9

count = 0
print("Entering A")
for i in range(0, large_num_rows, large_sudoku_cell_size):
    for j in range(0, large_num_columns, large_sudoku_cell_size):
        if i + large_sudoku_cell_size <= large_num_rows and j + large_sudoku_cell_size <= large_num_columns:
            cell = large_sudoku_img[i: i + large_sudoku_cell_size, j: j + large_sudoku_cell_size]

            # cv.imshow("", cell)
            # cv.waitKey(0)
            a = pt.image_to_string(cell, config='--psm 6 -c tessedit_char_whitelist=123456789')
            if a != "":
                sudoku_board[count] = a
            count = count + 1
print("Exiting A")

sudoku = np.reshape(sudoku_board, (-1, 9))
print(sudoku)
print(len([i for i in sudoku_board if i != 0]))
