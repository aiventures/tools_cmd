""" template code for argparse """

# https://stackoverflow.com/questions/19124304/what-does-metavar-and-action-mean-in-argparse-in-python
# https://stackoverflow.com/questions/27694032/difference-between-default-and-store-const-in-argparse
# https://stackoverflow.com/questions/20165843/argparse-how-to-handle-variable-number-of-arguments-nargs

import sys
import argparse
from pathlib import Path
import os
parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="StartPath",metavar='File Path')

parser.add_argument('--save',"-s", dest='save', action='store_true',help="Save")
parser.add_argument('--no-save',"-nos", dest='save', action='store_false',help="Do not save")
parser.set_defaults(save=True)

parser.add_argument('--debug',"-c", dest='debug', action='store_true',help="Show debug Info")
parser.add_argument('--no-debug',"-nc", dest='debug', action='store_false',help="Do not show debug info")
parser.set_defaults(debug=False)

parser.add_argument("--exiftool","-et",default="exiftool.exe",help="Exiftool Executable",metavar='Exiftool Executable')


#parser.add_argument("-optparam2",default=2.0,help="help text (int)",type=float,metavar='myvar')
#parser.add_argument("--opt_param","-o",action="store_true",help="help text")
#parser.add_argument("--path",default="",help="help text")
#parser.add_argument("--mult",default="",nargs='+',help="help text")
# python argparse_
# test.py 4 --path="n" --m_args dsdsd sdd wegg
# bool handling not out of the box

# parser.add_argument('--debug',"-c", dest='debug', action='store_true',help="Show debug Info")
# parser.add_argument('--no-debug',"-nc", dest='debug', action='store_false',help="Do not show debug info")
# parser.set_defaults(debug=False)

# parser.add_argument("-maxlevel",default=1,help="Maximum folder level to be read",type=int,metavar='Maximum Folder Level')
# parser.add_argument("--exif_command","-t",default=exif_command,nargs='*',help="EXIF command for read",metavar="EXIF exif_command for read")
# parser.add_argument("--filetypes","-t",default=[],nargs='*',help="File Extensions for filter",metavar='File Extensions')
# bool handling not out of the box
#parser.add_argument("-optparam2",default=2.0,help="help text (int)",type=float,metavar='myvar')
#parser.add_argument("--opt_param","-o",action="store_true",help="help text")
#parser.add_argument("--mult",default="",nargs='+',help="help text")
# python argparse_
# test.py 4 --path="n" --m_args dsdsd sdd wegg
# parser.add_argument("--filetypes","-t",default=[],nargs='*',help="File Extensions for filter",metavar='File Extensions')

# parser.add_argument('--descriptions',"-d", dest='descriptions', action='store_true',help="Save image descriptions to target path as text file")
# parser.add_argument('--no-descriptions',"-nd", dest='descriptions', action='store_false',help="Do not save image descriptions")
# parser.set_defaults(descriptions=True)
# parser.add_argument("--target_path","-tp",default=None,help="Location of save files with None as original path",metavar='target path')

args = parser.parse_args()
print(f"Arguments {args}")
p=args.path
save=args.save
debug=args.debug
exiftool=args.exiftool

if os.path.isdir(p):
    p=Path(p).absolute()
    print(f"Using Path {root_path}")
    pass
else:
    print(f"{p} is not a valid path")
    sys.exit()

# do the other stuff 