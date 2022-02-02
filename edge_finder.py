import cv2  # type: ignore
import numpy
import numpy.typing


def find_edges(
    image: numpy.typing.NDArray,
    thresh: int,
    ratio: int,
    kernel_size: int,
    matrix: tuple[int, int],
) -> numpy.typing.NDArray:
    img_blur = cv2.blur(image, matrix)
    return cv2.Canny(img_blur, thresh, thresh * ratio, kernel_size)


def get_image_edges(
    image: numpy.typing.NDArray,
    thresh=75,
    ratio: int = 3,
    kernel_size: int = 3,
    matrix: tuple[int, int] = (3, 3),
) -> numpy.typing.NDArray:
    grayscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_edges = find_edges(image, thresh, ratio, kernel_size, matrix)
    # Returns a 2D array
    return img_edges
