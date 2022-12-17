import pathlib
import sys
from handlers import process_input_filepath, process_input, process_read_file, LOGGER
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
    return parser.parse_args()


def main():
    args = parse_arguments()
    print(args)
    env_filepath = args.filename # 'input/structure.txt' #input/structure.json, process_input_filepath()
    # env_output_filename = args.output_filename
    # env_debug = args.debug
    input_suffix = pathlib.Path(env_filepath).suffix
    process_input(input_suffix, env_filepath)
    process_read_file(env_filepath)


if __name__ == "__main__":
    main()
