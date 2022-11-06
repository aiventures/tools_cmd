""" moves images of manual lenses into new folder """

import sys
import argparse
from pathlib import Path
import os
from tools import img_file_info_xls as im

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="StartPath",metavar='File Path')
parser.add_argument('--save',"-s", dest='save', action='store_true',help="Save")
parser.add_argument('--no-save',"-nos", dest='save', action='store_false',help="Do not save")
parser.set_defaults(save=True)
parser.add_argument('--debug',"-c", dest='debug', action='store_true',help="Show debug Info")
parser.add_argument('--no-debug',"-nc", dest='debug', action='store_false',help="Do not show debug info")
parser.set_defaults(debug=False)

args = parser.parse_args()
print(f"Arguments {args}")
p=args.path
save=args.save
debug=args.debug

if os.path.isdir(p):
    p=str(Path(p).absolute())
    print(f"Using Path {p}")
    pass
else:
    print(f"{p} is not a valid path")
    sys.exit()

# do the other stuff 
im.move_manual_images(fp=p,debug=debug,save=save)
