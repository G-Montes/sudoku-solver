import cv2  # type: ignore
import numpy
import numpy.typing


def find_sudoku_board_corner(
    image: numpy.typing.NDArray, color_pixel_ratio: float = 0.75
) -> "tuple[int, int]":
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


def find_intersections(
    image: numpy.typing.NDArray, threshold: int = 0.75
) -> numpy.typing.NDArray:
    horiz_lines = numpy.empty(image.shape, dtype=numpy.float32)
    vert_lines = numpy.empty(numpy.transpose(image).shape, dtype=numpy.float32)
    for index, row in enumerate(image):
        if numpy.any(row) and ((numpy.count_nonzero(row) / row.shape[0]) >= threshold):
            horiz_lines[index] = row
    for index, row in enumerate(numpy.transpose(image)):
        if numpy.any(row) and ((numpy.count_nonzero(row) / row.shape[0]) >= threshold):
            vert_lines[index] = row
    vert_lines = numpy.transpose(vert_lines)

    intersections = numpy.empty(image.shape, dtype=numpy.float32)
    for row_indx, row in enumerate(image):
        for col_indx, _ in enumerate(row):
            if (
                horiz_lines[row_indx][col_indx] != 0 or vert_lines[row_indx][col_indx]
            ) and horiz_lines[row_indx][col_indx] == vert_lines[row_indx][col_indx]:
                intersections[row_indx][col_indx] = 255.0

    cv2.imshow("horiz", horiz_lines)
    cv2.imshow("vert", vert_lines)
    cv2.imshow("intersection", intersections)
    return intersections
