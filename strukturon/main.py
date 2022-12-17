import pathlib
import sys
from handlers import process_input_filepath, process_input, process_read_file
from logger import LOGGER
from argparse import ArgumentParser, Namespace


def parse_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-f",
        "--filename",
        required=True
    )
    parser.add_argument(
        "-o",
        "--output-filename",
        required=True
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=False
    )
    parser.add_argument(
        "-i",
        "--input",
        action="store_true",
        default=False
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    # print(args.output_filename)
    # exit(1)
    env_filepath = args.filename  # filepath to process
    env_output_filename = args.output_filename
    env_debug = args.debug  # if to show debug
    env_input = args.input  # set to display input to process
    input_suffix = pathlib.Path(env_filepath).suffix
    if env_input is True:
        process_read_file(env_filepath)
    process_input(input_suffix, env_filepath, env_output_filename, env_debug)


if __name__ == "__main__":
    main()
