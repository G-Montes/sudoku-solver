import json
import os

import cv2
import numpy.typing


def show_image(img: numpy.typing.NDArray, name: str = "") -> None:
    cv2.imshow(name, img)


def load_img(image_path: str) -> numpy.typing.NDArray:
    image = cv2.imread(image_path)
    if image is None:
        raise Exception("Something went wrong with the image loading.")
    else:
        return image


def get_image_path(image_name: str, use_solved_folder: bool) -> str:
    cwd = os.getcwd()
    config = open("config.json", "r")
    config_data = json.load(config)
    folder_name = (
        config_data["solved_folder"]
        if use_solved_folder
        else config_data["unsolved_folder"]
    )
    return cwd + folder_name + image_name
