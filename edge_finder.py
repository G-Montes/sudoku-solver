import cv2 as cv  # type: ignore
import numpy as np
import numpy.typing as npt


def find_edges(
    image: npt.NDArray,
    thresh: int,
    ratio: int,
    kernel_size: int,
    matrix: tuple[int, int],
) -> npt.NDArray:
    img_blur = cv.blur(image, matrix)
    return cv.Canny(img_blur, thresh, thresh * ratio, kernel_size)


def find_sudoku_board_corner(image: npt.NDArray) -> tuple[int, int]:
    for row_index, row in enumerate(image):
        if np.any(row) and np.mean([x if x == 0 else 1 for x in row]) > 0.6:
            return (row_index, np.where(row != 0)[0][0])

    return (0, 0)  # No suitable corner found


def crop_to_sudoku_border(image: npt.NDArray) -> npt.NDArray:
    num_rows, num_cols = image.shape
    top_left_corner = find_sudoku_board_corner(image)
    reversed_img = image[::-1, ::-1]
    bottom_right_corner = find_sudoku_board_corner(reversed_img)
    return image[
        top_left_corner[0] : num_rows - bottom_right_corner[0],
        top_left_corner[1] : num_cols - bottom_right_corner[1],
    ]


def get_image_edges(
    image: npt.NDArray,
    thresh=75,
    ratio: int = 3,
    kernel_size: int = 3,
    matrix: tuple[int, int] = (3, 3),
) -> npt.NDArray:
    grayscale_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img_edges = find_edges(image, thresh, ratio, kernel_size, matrix)

    # Returns a 2D array
    return img_edges
