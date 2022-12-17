from typing import Optional
from json_file_handler import process_json
from logger import LOGGER


OUTPUT_PATH_HTML = '../output/output.html'  # FIXME: add as arg


def process_input_filepath(input_data_file: list[str]) -> Optional[str]:
    """ Takes input data file to process.

    :param input_data_file: Data of input file.
    :return: none or data.
    """

    if input_data_file is not None:
        return input_data_file[1]
    return None


def process_read_file(input_file_name_path: str):
    """ Reads file source

    :param input_file_name_path: data of give file in given path
    :return: none or data.
    """

    with open(input_file_name_path, 'r') as f:
        lines = f.readlines()
        print(lines)


def perform_html_output(html_input: str, output_data_file: str):
    """ Performs HTML output write to file

    :param html_input: HTML data structure to write to file
    :param output_data_file: target file path to write to file
    :return: none or data.
    """

    LOGGER.info("writing out HTML into "+output_data_file+" file")
    func = open(output_data_file, "w")
    func.write(html_input)
    func.close()


def process_input(input_suffix: str, input_data_file: str, output_data_file: str, show_debug: bool):
    """ Processes input by its suffix

    :param input_suffix: file input format
    :param input_data_file: data of given file
    :param output_data_file: target filepath
    :param show_debug: debug info display
    :return: none or data.
    """

    if show_debug is True:
        import pdb
        pdb.set_trace()

    if input_suffix == '.txt':
        LOGGER.info("is TEXT file type")
        # process_txt(input_data_file)
    elif input_suffix == '.json':
        LOGGER.info("is JSON file type")
        data_process_return = process_json(input_data_file)
        if type(data_process_return) == str and len(data_process_return) > 0:
            perform_html_output(data_process_return, output_data_file)
    elif input_suffix == '.xml':
        LOGGER.info("is XML file type")
        # process_xml(input_data_file)
    else:
        LOGGER.error("unknown file type")

