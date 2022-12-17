from json2html import *
from typing import Optional
import json
from logging import getLogger, DEBUG, basicConfig
# json.JSONDecodeError # TODO: test with possible UCS

OUTPUT_PATH_HTML = '../output/output.html'  # FIXME: add as arg

LOGGER = getLogger("Strukturon")
LOGGER.setLevel(DEBUG) # TODO: set level dynamically according to call
basicConfig()

def process_input_filepath(input_data_file: list[str]) -> Optional[str]:
    """ Takes input data file to process.

    :param input_data_file: Data of input file.
    :return: none or data.
    """

    if input_data_file is not None:
        return input_data_file[1]
    return None


def process_json(inputDataFile: str):

    try:
        with open(inputDataFile, "r") as input_file:
            input_content = input_file.read()
    except FileNotFoundError as e:
        LOGGER.error("file not found") # raise # pass # print(e)

    returnProcessJson = json2html.convert(
        json=json.loads(input_content))  # json.loads - načítá string, load chce file descriptor
    # TODO: process check of validity of JSON as above with try & except -

    perform_html_output(returnProcessJson)
    # performHTMLOutput(json2html.convert(json = inputDataFile))


def process_read_file(inputFileNamePath: str):
    # print(inputFileNamePath)
    # exit(1)

    with open(inputFileNamePath, 'r') as f:
        lines = f.readlines()
        # print(lines)


def perform_html_output(htmlInput: str):
    Func = open(OUTPUT_PATH_HTML, "w")
    Func.write(htmlInput)
    Func.close()


def process_input(inputSuffix: str, inputDataFile: str):
    # import pdb
    # pdb.set_trace()
    if inputSuffix == '.txt':
        # print("is text")
        LOGGER.info("is text")
    elif inputSuffix == '.json':
        LOGGER.info("is json")
        process_json(inputDataFile)
    else:
        print("unknown file type")

