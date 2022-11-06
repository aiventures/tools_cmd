""" video files rename based on regex, new version """
import sys
import argparse
from pathlib import Path
import os
#from importlib import reload
#import tools.video_rename_v2
#reload(tools.video_rename_v2)
from tools import file_module as fm
from tools import video_rename_v2 as vr

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="StartPath",metavar='File Path')

# debug flag
parser.add_argument('--debug',"-d", dest='debug', action='store_true',help="Show debug Info")
parser.add_argument('--no-debug',"-nd", dest='debug', action='store_false',help="Do not show debug info")
parser.set_defaults(debug=False)

# save_file_info info: save metadata information as json into subfolders
parser.add_argument('--save_file_info',"-i", dest='save_file_info', action='store_true',help="save metadata from info file as json")
parser.add_argument('--no-save_file_info',"-ni", dest='save_file_info', action='store_false',help="Do not save metadata from info file as json")
parser.set_defaults(save_file_info=True)


# multiple arguments call as params without brackets !
parser.add_argument("--ignore_paths","-ip",default=["kopiert"],nargs='*',help="Folders to be ignored",metavar='Folder Ignore')
parser.add_argument("--ignore_files","-if",default=["cleanup","file_info"],nargs='*',help="Files not to be processed",metavar='Files Ignore')
parser.add_argument("--file_types","-t",default=["txt","mp4"],nargs='*',help="Filetypes to be processed",metavar='Filetypes')

args = parser.parse_args()
print("*** READING FILE INFO ")
print(f"Arguments {args}")

p=args.path
debug=args.debug
filetypes=args.file_types
save_file_info=args.save_file_info
ignore_paths=args.ignore_paths
ignore_files=args.ignore_files
file_types=args.file_types

if os.path.isdir(p):
    root_path=str(Path(p).absolute())
    print(f"Using Path {root_path}")
else:
    print(f"ERROR: {p} is not a valid path")
    sys.exit()

info_dict=fm.read_file_info(p,type_filters=filetypes)
rename_dict=vr.rename_video_files(info_dict,debug=debug,ignore_folders=ignore_paths,ignore_files=ignore_files,save_file_info=save_file_info)
# idea: implement undo function using rename dict







