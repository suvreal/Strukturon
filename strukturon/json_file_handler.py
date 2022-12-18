import json
from json2html import *
from logger import LOGGER


def process_json(input_data_file: str):
    """ Processes input JSON structure into a HTML

    :param input_data_file: data of given file in JSON to be transformed into HTML
    :return: none or data.
    """

    try:
        with open(input_data_file, "r", encoding='UTF-8') as input_file:
            input_content = input_file.read()
    except FileNotFoundError as e:
        LOGGER.error("file not found")
        return None

    try:
        json.loads(input_content)
    except ValueError as e:
        LOGGER.error("file not valid JSON")
        return None

    return_process_json = json2html.convert(json=json.loads(input_content))
    return return_process_json
