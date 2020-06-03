import sys
import cv2 as cv
import numpy

sudoku_img_path = r"C:\\Users/genar/Documents/431.jpg"
THRESHOLD = 75

def show_image(image):
    cv.imshow("", image)
    cv.waitKey(0)

def load_img(image_path):
    image = cv.imread(sudoku_img_path)
    if image is None:
        raise Exception("Something went wrong with the image loading.")
    else:
        return image

def get_edges(thresh):
    ratio = 3
    kernel_size = 3 
    matrix = (3, 3)
    img_blur = cv.blur(sudoku_img_gray, matrix)
    detected_edges = cv.Canny(img_blur, thresh, thresh * ratio, kernel_size)
    mask = detected_edges != 0
    edges = sudoku_img * (mask[:,:, None].astype(sudoku_img.dtype))
    return edges

def find_sudoku_board_corner(image):
    for row_index, row in enumerate(image):
        if numpy.any(row):
            for col_index, element in enumerate(row):
                if element != 0:
                    print(row_index, col_index)
                    return (row_index, col_index)

def crop_to_sudoku_border(image):
    num_rows, num_cols = image.shape
    top_left_corner =  find_sudoku_board_corner(image)
    reversed_img = image[::-1,::-1]
    bottom_right_corner = find_sudoku_board_corner(reversed_img)
    
    return image[top_left_corner[0]:num_rows - bottom_right_corner[0], top_left_corner[1]: num_cols - bottom_right_corner[1]]

sudoku_img = load_img(sudoku_img_path)
sudoku_img_gray = cv.cvtColor(sudoku_img, cv.COLOR_BGR2GRAY)
sudoku_img_edges = get_edges(THRESHOLD)
altered = sudoku_img_edges[:,:,0]
cropped_image = crop_to_sudoku_border(altered)
print(cropped_image.shape)
show_image(cropped_image)