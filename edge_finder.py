import sys
import cv2 as cv
import numpy
import os

cwd = os.getcwd()
image_folder = "/unsolved-images/"
file_name = "unsolved_1.png"
sudoku_img_path = cwd + image_folder + file_name

THRESHOLD = 75


def show_image(image, name=""):
    cv.imshow(name, image)


def load_img(image_path):
    image = cv.imread(sudoku_img_path)
    if image is None:
        raise Exception("Something went wrong with the image loading.")
    else:
        return image


def get_edges(image, thresh=THRESHOLD):
    ratio = 3
    kernel_size = 3
    matrix = (3, 3)
    img_blur = cv.blur(image, matrix)
    detected_edges = cv.Canny(img_blur, thresh, thresh * ratio, kernel_size)
    mask = detected_edges != 0
    edges = sudoku_img * (mask[:, :, None].astype(sudoku_img.dtype))
    return edges


def find_sudoku_board_corner(image):
    for row_index, row in enumerate(image):
        if numpy.any(row) and numpy.mean([x if x == 0 else 1 for x in row]) > 0.6:
            return (row_index, numpy.where(row != 0)[0][0])


def crop_to_sudoku_border(image):
    num_rows, num_cols = image.shape
    top_left_corner = find_sudoku_board_corner(image)
    reversed_img = image[::-1, ::-1]
    bottom_right_corner = find_sudoku_board_corner(reversed_img)

    return image[
        top_left_corner[0] : num_rows - bottom_right_corner[0],
        top_left_corner[1] : num_cols - bottom_right_corner[1],
    ]


sudoku_img = load_img(sudoku_img_path)
sudoku_img_gray = cv.cvtColor(sudoku_img, cv.COLOR_BGR2GRAY)
sudoku_img_edges = get_edges(sudoku_img_gray)
altered = sudoku_img_edges[:, :, 0]
show_image(sudoku_img_edges, name="original")
show_image(altered, name="altered")
cv.waitKey(0)
