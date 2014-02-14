apStringToLocalizable
=====================

covert Excel file to localizable files

Requirements
=====

* xlrd

Usage
=====

    usage: apStringToLocalizable.py [-h] [-l LOCALIZABLE_FOLDER] [-f LOCALIZABLE_FILE] [-q]
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
