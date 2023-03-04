""" changes metadata for given path / file """

import sys
import argparse
from pathlib import Path
import os
from tools import img_file_info_xls as im

# metadata_information
LENS_INFO={"trio":im.EXIF_LENS_LENSBABY_TRIO}
lens_dict ={}
print("Add EXIF: Choose Lens Info:")
for i,lens in enumerate(im.EXIF_LENSES):
    print(f"[{str(i).zfill(2)}]: {lens}")
    lens_dict[str(i)]=im.EXIF_LENSES[lens]
l_index=input("Enter Lens # (blank=0): ")
if not l_index:
    l_index="0"
lens_info=lens_dict.get(l_index)
if not lens_info:
    print("No valid lens info selected")
    sys.exit(1)

print(f"Lens Data: {lens_info}")

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="StartPath",metavar='File Path')

parser.add_argument('--save',"-s", dest='save', action='store_true',help="Save")
parser.add_argument('--no-save',"-nos", dest='save', action='store_false',help="Do not save")
parser.set_defaults(save=True)

parser.add_argument('--debug',"-c", dest='debug', action='store_true',help="Show debug Info")
parser.add_argument('--no-debug',"-nc", dest='debug', action='store_false',help="Do not show debug info")
parser.set_defaults(debug=False)

parser.add_argument("--exiftool","-et",default="exiftool.exe",help="Exiftool Executable",metavar='Exiftool Executable')

args = parser.parse_args()
print(f"Arguments {args}")
p=args.path
save=args.save
debug=args.debug
exiftool=args.exiftool

if os.path.isdir(p):
    p=str(Path(p).absolute())
    print(f"Using Path {p}")
    pass
else:
    print(f"{p} is not a valid path")
    sys.exit()

# do the other stuff 
im.change_metadata(p,exif_attribute_dict=lens_info,save=save,exiftool=exiftool,debug=debug)