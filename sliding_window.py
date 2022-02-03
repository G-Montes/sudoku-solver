import cv2 as cv  # type: ignore
import numpy
import numpy.typing

import corner_finder
import edge_finder
import image_utils


def find_boxes(sudoku_img: numpy.typing.NDArray) -> "tuple[int, int]":
    # TODO: Add functionality to detect boundaries of a sudoku box
    edges = edge_finder.get_image_edges(sudoku_img)
    corners = corner_finder.find_harris_corners(edges)
    edge = corner_finder.find_intersections(edges)

    # image_utils.show_image(edges, "edges")
    # image_utils.show_image(corners, "corners")
    # image_utils.show_image(edge, "intersection")
    cv.waitKey(0)

    return (0, 0)


image_path = image_utils.get_image_path("solved_1.png", use_solved_folder=True)
sudoku_image = image_utils.load_img(image_path)
find_boxes(sudoku_image)
