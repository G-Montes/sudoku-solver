import os
import json
import cv2 as cv
import numpy.typing as npt


def show_image(img: npt.NDArray, name: str = "") -> None:
    cv.imshow(name, img)


def load_img(image_path: str) -> npt.NDArray:
    image = cv.imread(image_path)
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
