from edge_finder import get_image_edges
from image_utils import get_image_path, show_image, load_img
import cv2 as cv

image_path = get_image_path("unsolved_1.png", use_solved_folder=False)
image = load_img(image_path)
edges = get_image_edges(image)
show_image(image, "oh")
show_image(edges, "flask")
cv.waitKey(0)
