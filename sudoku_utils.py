import os
import json


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
