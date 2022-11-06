""" template code for argparse """

# https://stackoverflow.com/questions/19124304/what-does-metavar-and-action-mean-in-argparse-in-python
# https://stackoverflow.com/questions/27694032/difference-between-default-and-store-const-in-argparse
# https://stackoverflow.com/questions/20165843/argparse-how-to-handle-variable-number-of-arguments-nargs


import os
import sys
import argparse
from pathlib import Path
from tools import img_file_info_xls as img_file

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default="metadata.tpl",help="path to config file",metavar='Image Configuration File (default metadata.tpl)')

# show detailed output
parser.add_argument('--debug',"-d", dest='debug', action='store_true',help="Show debug Info")
parser.add_argument('--no-debug',"-nd", dest='debug', action='store_false',help="Do not show debug info")
parser.set_defaults(debug=True)

# show detailed output
parser.add_argument('--geo',"-g", dest='geo', action='store_true',help="Get geo location info from nominatim reverse search")
parser.add_argument('--no-geo',"-ng", dest='geo', action='store_false',help="Do not get geo location info from nominatim reverse search")
parser.set_defaults(geo=True)

args = parser.parse_args()
print(f"Arguments {args}")

fp=args.path
debug=args.debug
geo=args.geo

# save=args.save

# exiftool=args.exiftool

if os.path.isfile(fp):
    fp=Path(fp).absolute()
    print(f"Using File {fp}")
    pass
else:
    print(f"{fp} is not a valid file")
    sys.exit()

img_file.update_img_meta_config(fp_config=fp,geo=geo,show=debug)