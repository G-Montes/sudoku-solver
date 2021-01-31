
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

def get_edges(src, should_track_horiz, struct_scale = 15, iter = 1):
    edges = np.copy(src)
    img_size = edges.shape[should_track_horiz]
    line_size = img_size // struct_scale

    if should_track_horiz:
        line_struct  = cv.getStructuringElement(cv.MORPH_RECT, (line_size, 1))
    else:
        line_struct  = cv.getStructuringElement(cv.MORPH_RECT, (1, line_size))

    edges = cv.erode(edges,line_struct)
    edges = cv.dilate(edges,line_struct, iterations = iter)

    return edges    

def find_sudoku_board_corner(image):
    for row_index, row in enumerate(image):
        if np.any(row):
            for col_index, element in enumerate(row):
                if element != 0:
                    return (row_index, col_index)

def crop_to_sudoku_border(edges_img, img_to_crop):
    num_rows, num_cols = edges_img.shape
    top_left_corner =  find_sudoku_board_corner(edges_img)
    reversed_img = edges_img[::-1,::-1]
    bottom_right_corner = find_sudoku_board_corner(reversed_img)
    
    return img_to_crop[top_left_corner[0]:num_rows - bottom_right_corner[0], top_left_corner[1]: num_cols - bottom_right_corner[1]]

def find_color_values(image):
    color_counts= {}
    for row in sudoku_img:
        for x in row:
            color_counts[x] = color_counts.get(x, 0) + 1
    
    return color_counts

def print_color_values(color_values):
    for i in sorted (color_values):
        print((i, color_values[i]), end=" ")

# Load and prep image for edge detection
sudoku_img = load_img(SUDOKU_IMG_PATH)
ret, inv_thresh_img = cv.threshold(sudoku_img, THRESHOLD, 255, cv.THRESH_BINARY_INV)
inv_img = cv.bitwise_not(inv_thresh_img)

# Edge Finding process
horiz_edges = get_edges(np.copy(inv_thresh_img), 1)
vert_edges = get_edges(np.copy(inv_thresh_img), 0)
edges = horiz_edges + vert_edges

sudoku_img = inv_img + edges

sudoku_img = crop_to_sudoku_border(edges, sudoku_img)

show_img(sudoku_img)
cv.waitKey(0)