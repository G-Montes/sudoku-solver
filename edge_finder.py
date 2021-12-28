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
