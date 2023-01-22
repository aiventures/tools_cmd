""" copies image metadata from one source file to other files belonging to a file group """

# example: use img_copy_metadata_from_img -a -f pureshot to copy metadata from files containing pureshot 

import sys
import argparse
from pathlib import Path
import os
# from tools import file_module as fm
from tools import img_file_info_xls as im

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="StartPath",metavar='File Path')

# bool handling not out of the box
parser.add_argument('--debug',"-d", dest='debug', action='store_true',help="Debug/Verbose information)")
parser.add_argument('--no-debug',"-nd", dest='debug', action='store_false',help="No Debug Information")
parser.set_defaults(debug=True)

# check if attribute exists, other attribute could be copyright to check if data were copied
parser.add_argument("--exif_attributes","-a",default=["Model"],nargs='*',help="Exif attributes for check for source files",metavar='Exif Attributes')
# special signatures like "source" to identify source files
parser.add_argument("--filename_signatures","-f",default=[],nargs='*',help="File name signatures to identify files with metadata",metavar='File Name Signature')
# suffix list: only files will be check having this suffix
parser.add_argument("--filename_suffixes","-fs",default=[],nargs='*',help="File suffix to be used (empty if all suffixes are to be checked)",metavar='File Suffix List')

args = parser.parse_args()
print("*** READING FILE INFO ")
print(f"Arguments {args}")

p=args.path
debug=args.debug
# file needs to contain a list of metadata attributes to count as metadata provider
marker_exif_attributes=args.exif_attributes
# # list that contains parts of file names to be considered as markers for source files
filename_signatures=args.filename_signatures
filename_suffixes=args.filename_suffixes

if os.path.isdir(p):
    root_path=Path(p).absolute()
    print(f"Using Path {root_path}")
else:
    print(f"{p} is not a valid path")
    sys.exit()

# read all metadata recursively / jpg only
metadata_dict=im.exiftool_get_path_dict(root_path,suffix_list=filename_suffixes)

# right now, only consider jpg files to copy metadata
target_filetypes=["jpg"]

copy_dict=im.get_copy_dict(metadata_dict,marker_exif_attributes,filename_signatures,debug=debug)
num_files=im.copy_metadata(copy_dict,display=True,save=False)
if num_files > 0 and input("copy metadata files? (y)")=="y":
    im.copy_metadata(copy_dict,display=False,save=True,debug=True,target_filetypes=target_filetypes)
else:
    print(f"Nothing done, {num_files} file metadata were not changed")
