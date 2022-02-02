import cv2  # type: ignore
import numpy
import numpy.typing


def find_sudoku_board_corner(
    image: numpy.typing.NDArray, color_pixel_ratio: float = 0.5
) -> tuple[int, int]:
    coord = [0, 0]  # Default if no suitable corner found
    for row_index, row in enumerate(image):
        # Checks if non-black pixel present in row & that non-black pixel ratio is over threshold
        # Reduces chance noise will get marked as corner.
        if (
            numpy.any(row)
            and numpy.count_nonzero(row) / image.shape[0] > color_pixel_ratio
        ):
            coord[0] = row_index
            break
    for row_index, row in enumerate(image.transpose()):
        if (
            numpy.any(row)
            and numpy.count_nonzero(row) / image.shape[1] > color_pixel_ratio
        ):
            coord[1] = row_index
            break
    return tuple(coord)


def crop_to_sudoku_border(image: numpy.typing.NDArray) -> numpy.typing.NDArray:
    num_rows, num_cols = image.shape
    top_left_corner = find_sudoku_board_corner(image)
    bottom_right_corner = find_sudoku_board_corner(image[::-1, ::-1])

    return image[
        top_left_corner[0] : num_rows - bottom_right_corner[0],
        top_left_corner[1] : num_cols - bottom_right_corner[1],
    ]


def find_harris_corners(image: numpy.typing.NDArray) -> numpy.typing.NDArray:
    # conerHarris() takes single channel 8-bit or floating point img
    float_img = numpy.float32(image)
    float_img = cv2.erode(float_img, None)
    return cv2.cornerHarris(float_img, 2, 3, 0.04)
