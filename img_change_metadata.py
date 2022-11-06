""" changes metadata for given path / file """

import sys
import argparse
from pathlib import Path
import os
from tools import img_file_info_xls as im

# metadata_information
LENS_INFO={"trio":im.EXIF_LENS_LENSBABY_TRIO}

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="StartPath",metavar='File Path')

parser.add_argument('--save',"-s", dest='save', action='store_true',help="Save")
parser.add_argument('--no-save',"-nos", dest='save', action='store_false',help="Do not save")
parser.set_defaults(save=True)

parser.add_argument('--debug',"-c", dest='debug', action='store_true',help="Show debug Info")
parser.add_argument('--no-debug',"-nc", dest='debug', action='store_false',help="Do not show debug info")
parser.set_defaults(debug=False)

parser.add_argument("--exiftool","-et",default="exiftool.exe",help="Exiftool Executable",metavar='Exiftool Executable')

parser.add_argument("--lens","-l",default="trio",help="Lens Specs (trio)",metavar='Lens Specs (trio)')

args = parser.parse_args()
print(f"Arguments {args}")
p=args.path
save=args.save
debug=args.debug
exiftool=args.exiftool
lens=args.lens
lens_specs=LENS_INFO.get(lens,None)
if not lens_specs:
    print(f"No lens specs found for {lens}, program end.")
    sys.exit()

if os.path.isdir(p):
    p=str(Path(p).absolute())
    print(f"Using Path {p}")
    pass
else:
    print(f"{p} is not a valid path")
    sys.exit()

# do the other stuff 
im.change_metadata(p,exif_attribute_dict=lens_specs,save=save,exiftool=exiftool,debug=debug)