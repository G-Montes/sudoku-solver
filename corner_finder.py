import numpy as np
import cv2 as cv  # type: ignore


def find_sudoku_board_corner(
    image: npt.NDArray, color_pixel_ratio: float = 0.5
) -> tuple[int, int]:
    coord = [0, 0]  # Default if no suitable corner found
    for row_index, row in enumerate(image):
        # Checks if non-black pixel present in row & that non-black pixel ratio is over threshold
        # Reduces chance noise will get marked as corner.
        if np.any(row) and np.count_nonzero(row) / image.shape[0] > color_pixel_ratio:
            coord[0] = row_index
            break
    for row_index, row in enumerate(image.transpose()):
        if np.any(row) and np.count_nonzero(row) / image.shape[1] > color_pixel_ratio:
            coord[1] = row_index
            break
    return tuple(coord)


def crop_to_sudoku_border(image: npt.NDArray) -> npt.NDArray:
    num_rows, num_cols = image.shape
    top_left_corner = find_sudoku_board_corner(image)
    bottom_right_corner = find_sudoku_board_corner(image[::-1, ::-1])

    return image[
        top_left_corner[0] : num_rows - bottom_right_corner[0],
        top_left_corner[1] : num_cols - bottom_right_corner[1],
    ]
