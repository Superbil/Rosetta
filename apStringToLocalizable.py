#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Superbil'
__version__ = '1.1.0'

import os
import xlrd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('book_file', help='appString file name')
parser.add_argument('-o', '--output_folder',
                    help='place to output', default=os.getcwd())
parser.add_argument('-l', '--localizable_folder',
                    help='output strings folder name',
                    default='Localizable')
parser.add_argument('-f', '--localizable_file',
                    help='output strings file name',
                    default='Localizable.strings')
parser.add_argument('-q', '--quite', help='quite run', action="store_true")
args = parser.parse_args()

context_line_format = '\"{0}\"=\"{1}\";'
language_map = {"Simplified Chinese": "zh-Hans.lproj",
                "Traditional Chinese": "zh-Hant.lproj",
                "English": "en.lproj",
                "French": "fr.lproj",
                "German": "de.lproj",
                "Italian": "it.lproj",
                "Spanish": "es.lproj",
                "Norweglan": "nb.lproj",
                "Dutch": "nl.lproj",
                "Hungarian": "hu.lproj",
                "Korean": "ko.lproj",
                "Japanese": "ja.lproj",
                "Portuguese": "pt.lproj",
                "Polish": "pl.lproj",
                "Turkish": "tr.lproj"}

book = xlrd.open_workbook(args.book_file, encoding_override='utf-8')
# always use first one
sh = book.sheet_by_index(0)

language = sh.row_values(0)
mls = sh.col_values(0)

for l in range(len(language)):

    # ID is not in language_map, pass it
    try:
        language_name = language_map[language[l]]

        if not args.quite:
            print '>> Working on {0}'.format(language_name)

        lang_base_folder = os.path.join(args.output_folder,
                                        args.localizable_folder)
        lang_folder = os.path.join(lang_base_folder, language_name)
        if not os.path.exists(lang_folder):

            if not args.quite:
                print ">> folder is not existes, create it"

            os.makedirs(lang_folder)

        lang_file = os.path.join(lang_folder, args.localizable_file)

        with open(lang_file, 'w') as f:

            for c in range(1, len(mls)):

                key = sh.cell_value(c, 0)
                # get value from sheet
                value = sh.cell_value(c, l)

                # check this line is comment
                if key[:2] == '//':

                    # don't insert space on first line
                    if c is not 1:
                        if not args.quite:
                            print ""
                        f.write('\n')

                    if not args.quite:
                        print key
                    f.write(key + '\n')

                else:
                    # null string will been pass
                    if key and value:

                        if not args.quite:
                            print context_line_format.format(key, value.encode('utf-8'))
                        f.write(context_line_format.format(key, value.encode('utf-8')) + '\n')

    except KeyError:
        pass
