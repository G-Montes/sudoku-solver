import cv2 as cv
import numpy

THRESHOLD = 75
window_name = 'Edge Map'
ratio = 3
kernel_size = 3 
matrix = (3, 3)
def get_edges(thresh):
    img_blur = cv.blur(src_gray, matrix)
    detected_edges = cv.Canny(img_blur, thresh, thresh * ratio, kernel_size)
    mask = detected_edges != 0
    edges = src * (mask[:,:, None].astype(src.dtype))
    cv.imshow(window_name, edges)
    return edges

img_path = r"C:\\Users/genar/Documents/431.jpg"
src = cv.imread(img_path)
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv. namedWindow(window_name)
edges_result = get_edges(THRESHOLD)
cv.waitKey(0)