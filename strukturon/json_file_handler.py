import json
from json2html import *
from logger import LOGGER


# json.JSONDecodeError # TODO: test with possible UCS


def process_json(input_data_file: str):
    """ Processes input JSON structure into a HTML

    :param input_data_file: data of given file in JSON to be transformed into HTML
    :return: none or data.
    """
    try:
        with open(input_data_file, "r") as input_file:
            input_content = input_file.read()
    except FileNotFoundError as e:
        LOGGER.error("file not found")  # raise # pass # print(e)

    return_process_json = json2html.convert(
        json=json.loads(input_content))  # TODO: process check of validity of JSON as above with try & except
    return return_process_json
