""" changes metadata for given path / file """

import sys
import logging
import argparse
from pathlib import Path
import os
from tools.img_analyzer import ImageAnalyzer


# metadata_information

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="StartPath",metavar='File Path')

# currently not used
parser.add_argument("--exiftool","-e",default="exiftool.exe",help="Exiftool Executable",metavar='Exiftool Executable')
parser.add_argument("--magick","-m",default="magick.exe",help="Magick Executable",metavar='Magick Executable')

args = parser.parse_args()
print(f"Arguments {args}")
p=args.path
exiftool=args.exiftool
magick=args.magick

if os.path.isdir(p):
    p=str(Path(p).absolute())
    print(f"Using Path {p}")
    pass
else:
    print(f"{p} is not a valid path")
    sys.exit()

# do the other stuff 
ImageAnalyzer(p).analyze()