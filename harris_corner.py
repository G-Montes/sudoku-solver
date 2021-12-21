from sudoku_utils import get_image_path

import numpy as np
import cv2 as cv

img_path = get_image_path("unsolved_1.png", use_solved_folder=False)

img = cv.imread(img_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 1, 0.04)

dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv.imshow(".git", img)
cv.waitKey(0)
