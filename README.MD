# STRUKTURON
A data structure transformation tool into HTML.

## Features:
- JSON to HTML structure transformation
- validity and transformability check

## Usage (CLI commands):
1. clone this repository
2. add your source JSON file for example "data.json" into root of app
3. use one of commands below (-d for debug and -i for input data writeout) - output.html will be automatically created/updated
```sh
python strukturon/main.py -f data.json -o output.html
python strukturon/main.py -f data.json -o output.html -d
python strukturon/main.py -f data.json -o output.html -i 
python strukturon/main.py -f data.json -o output.html -d -i 
```

## Future development
- XML and CSV support

## Author
SVRL