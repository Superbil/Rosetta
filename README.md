## Rosetta

Covert excel file to [localizable](https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPInternational/Articles/StringsFiles.html) files

## Requirements

* xlrd

## Install

    pip install -r requirements.txt

## Usage

    usage: rosetta.py [-h] [-l LOCALIZABLE_FOLDER] [-f LOCALIZABLE_FILE] [-q]
                      [-o OUTPUT_FOLDER]
                      book_file

    positional arguments:
      book_file             appString file name

    optional arguments:
      -h, --help            show this help message and exit
      -l LOCALIZABLE_FOLDER, --localizable_folder LOCALIZABLE_FOLDER
                            output strings folder name
      -f LOCALIZABLE_FILE, --localizable_file LOCALIZABLE_FILE
                            output strings file name
      -q, --quite           quite run
      -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                            place to output


## License

Rosetta is available under the GPL v3. See the LICENSE file for more info.
