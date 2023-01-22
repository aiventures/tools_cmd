""" 
    Utility to create resized images 
    using imagemagick 
    https://imagemagick.org/index.php
    (needs to covered in Path variable ) 
"""

import os
import argparse
import sys
# from tools.simple_input import v
from tools import img_file_info_xls as img_info
from pathlib import Path

# from _paths import exe_magick
# from _paths import exe_exiftool

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="Start Path",metavar='File Path')
parser.add_argument("-image_size","-is",default=1800,help="Resized Image Size",type=int,metavar='target image size')

parser.add_argument('--prefix',"-pf", dest='prefix', action='store_true',help="Write Image size as prefix")
parser.add_argument('--no-prefix',"-npf", dest='prefix', action='store_false',help="Write Image Size as suffix")
parser.set_defaults(prefix=True)

parser.add_argument("-quality","-iq",default=85,help="Output Image Quality",type=int,metavar='image quality')
parser.add_argument('--remove_metadata',"-rmd", dest='remove_metadata', action='store_true',help="Remove Metadata in resized image")
parser.add_argument('--keep_metadata',"-md", dest='remove_metadata', action='store_false',help="Keep Metadata in resized image")
parser.set_defaults(remove_metadata=True)

parser.add_argument("--magick","-m",default="magick.exe",help="magick.exe executable/location (needs to be in Win path)",metavar='magick exe')
parser.add_argument("--exiftool","-e",default="exiftool.exe",help="exiftool.exe executable/location (needs to be in Win path)",metavar='exiftool exe')

parser.add_argument('--save',"-s", dest='save', action='store_true',help="Save Images")
parser.add_argument('--no-save',"-nos", dest='save', action='store_false',help="Do not save images")
parser.set_defaults(save=True)

parser.add_argument('--descriptions',"-d", dest='descriptions', action='store_true',help="Save image descriptions to target path as text file")
parser.add_argument('--no-descriptions',"-nd", dest='descriptions', action='store_false',help="Do not save image descriptions")
parser.set_defaults(descriptions=True)

parser.add_argument("--target_path","-tp",default=None,help="Location of save files with None as original path",metavar='target path')

args = parser.parse_args()
print(f"Arguments {args}")

p=args.path
image_size=args.image_size
prefix=args.prefix
quality=args.quality
remove_metadata=args.remove_metadata
magick=args.magick
exiftool=args.exiftool
save=args.save
descriptions=args.descriptions
target_path=args.target_path

if os.path.isdir(p):
    root_path=Path(p).absolute()
    print(f"--- Resize images in folder: {p}")
else:
    print(f"{p} is not a valid path")
    sys.exit()

img_info.magick_resize( p,magick=magick,
                        exiftool=exiftool,
                        image_size=image_size,
                        quality=quality,prefix=prefix,
                        remove_metadata=remove_metadata,save=save,
                        descriptions=descriptions,
                        target_path=target_path)

input("enter key to exit")

