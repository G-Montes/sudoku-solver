import sys
import cv2 as cv
import numpy

sudoku_img_path = r"C:\\Users/genar/Documents/431.jpg"
THRESHOLD = 75

def show_image(image):
    cv.imshow("", image)
    cv.waitKey(0)

def load_img(image_path,use_grayscale = True):
    image = cv.imread(sudoku_img_path, 0 if use_grayscale else 1)
    
    if image is None:
        raise Exception("Something went wrong with the image loading.")
    else:
        return image

def get_edges(thresh, image):
    ratio = 3
    kernel_size = 3 
    matrix = (3, 3)
    img_blur = cv.blur(image, matrix)
    detected_edges = cv.Canny(img_blur, thresh, thresh * ratio, kernel_size)
    mask = detected_edges != 0
    edges = sudoku_img * (mask[:,:, None].astype(image.dtype))
    return edges

def find_sudoku_board_corner(image):
    for row_index, row in enumerate(image):
        if numpy.any(row):
            for col_index, element in enumerate(row):
                if element != 0:
                    return (row_index, col_index)

def crop_to_sudoku_border(image):
    num_rows, num_cols = image.shape
    top_left_corner =  find_sudoku_board_corner(image)
    reversed_img = image[::-1,::-1]
    bottom_right_corner = find_sudoku_board_corner(reversed_img)
    
    return image[top_left_corner[0]:num_rows - bottom_right_corner[0], top_left_corner[1]: num_cols - bottom_right_corner[1]]

sudoku_img = load_img(sudoku_img_path)
# sudoku_img_edges = get_edges(THRESHOLD, sudoku_img)

# contours, hierarchy = cv.findContours(sudoku_img, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

# cv.drawContours(sudoku_img, contours, -1, (0, 255, 0), 3)

# show_image(sudoku_img)

