
import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import resize
from matplotlib import pyplot as plt

SUDOKU_IMG_PATH = r"C:\\Users/genar/Documents/431.jpg"
THRESHOLD = 127
window_name = 0

def show_img(image):
    global window_name
    cv.imshow(str(window_name), image)
    window_name +=1

def load_img(image_path, use_grayscale = True):
    image = cv.imread(SUDOKU_IMG_PATH, 0 if use_grayscale else 1)
    
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

def find_color_values(image):
    color_counts= {}
    for row in sudoku_img:
        for x in row:
            color_counts[x] = color_counts.get(x, 0) + 1
    
    return color_counts

def print_color_values(color_values):
    for i in sorted (color_values):
        print((i, color_values[i]), end=" ")

sudoku_img = load_img(SUDOKU_IMG_PATH)
ret, inv_thresh_img = cv.threshold(sudoku_img, THRESHOLD, 255, cv.THRESH_BINARY_INV)
inv_img = cv.bitwise_not(inv_thresh_img)

STRUCT_EDGE_SCALE = 10

# horizontal
horiz_edges = np.copy(inv_thresh_img)
horiz_cols = horiz_edges.shape[1]
horiz_size = horiz_cols // STRUCT_EDGE_SCALE
horiz_struct = cv.getStructuringElement(cv.MORPH_RECT, (horiz_size, 1))

horiz_edges = cv.erode(horiz_edges, horiz_struct)
horiz_edges = cv.dilate(horiz_edges, horiz_struct, iterations = 1)

# vertical
vert_edges = np.copy(inv_thresh_img)
vert_rows = vert_edges.shape[0]
vert_size = vert_rows // STRUCT_EDGE_SCALE
vert_struct = cv.getStructuringElement(cv.MORPH_RECT, (1, vert_size))

vert_edges = cv.erode(vert_edges, vert_struct)
vert_edges = cv.dilate(vert_edges, vert_struct, iterations = 1)

# combined edges
edges = horiz_edges + vert_edges

cv.waitKey(0)