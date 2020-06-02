import sys
import cv2 as cv
import numpy

sudoku_img_path = r"C:\\Users/genar/Documents/431.jpg"
THRESHOLD = 75

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

sudoku_img = load_img(sudoku_img_path)
sudoku_img_gray = cv.cvtColor(sudoku_img, cv.COLOR_BGR2GRAY)
sudoku_img_edges = get_edges(THRESHOLD)
altered = sudoku_img_edges[:,:,0]
print(altered.shape)
cv.imshow("image", altered)
cv.waitKey(0)

            