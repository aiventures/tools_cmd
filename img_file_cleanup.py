""" cleaning up collateral image files / eventually raw as well """

# # example: use img_copy_metadata_from_img -a -f pureshot to copy metadata from files containing pureshot 
import sys
import argparse
from pathlib import Path
import os
from tools import img_file_cleanup_util as file_cleanup

# create your own file _img_file_settings and create 
# list of folders that you do not wantr to use for gps analysis
# only substring of folder path is sufficient
# leave empty if you want to use all folders
# IGNORE_FOLDERS_GPX=["FOLDER","..."]
from _img_file_settings import IGNORE_FOLDERS_GPX

# file location of the exiftool waypoint transformation file
# https://exiftool.org/geotag.html
# https://github.com/exiftool/exiftool/blob/master/fmt_files/gpx_wpt.fmt
# CMD_EXIF_WAYPT_FMT=r'C:\...\exiftool_wpt.fmt'
from  _img_file_settings import CMD_EXIF_WAYPT_FMT
# Name of Subfolder containing JPGs (eg "POST")
from  _img_file_settings import JPG_FOLDER_WAYPT
# location of exiftool if in path it is "exiftool.exe"
from  _img_file_settings import CMD_EXIFTOOL

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="StartPath",metavar='File Path')

# bool handling not out of the box
parser.add_argument('--debug',"-d", dest='debug', action='store_true',help="Debug/Verbose information)")
parser.add_argument('--no-debug',"-nd", dest='debug', action='store_false',help="No Debug Information")
parser.set_defaults(debug=True)

# saving
parser.add_argument('--save',"-s", dest='save', action='store_true',help="Save Changes")
parser.add_argument('--no-save',"-ns", dest='save', action='store_false',help="Do not save")
parser.set_defaults(save=True)

# verbose output
parser.add_argument('--verbose',"-v", dest='verbose', action='store_true',help="Verbose output")
parser.add_argument('--no-output',"-nv", dest='verbose', action='store_false',help="No output")
parser.set_defaults(verbose=True)

# delete collateral files
parser.add_argument('--collateral',"-c", dest='collaterals', action='store_true',help="Delete Collateral Files")
parser.add_argument('--no-collateral',"-nc", dest='collaterals', action='store_false',help="Do Not Delete Collateral Files")
parser.set_defaults(collaterals=True)

# delete raw files
parser.add_argument('--raw',"-r", dest='raw', action='store_true',help="Delete RAW Files")
parser.add_argument('--no-raw',"-nr", dest='raw', action='store_false',help="Do Not Delete RAW Files")
parser.set_defaults(raw=True)

# move files
parser.add_argument('--move',"-m", dest='move', action='store_true',help="MOVE Files")
parser.add_argument('--no-move',"-nm", dest='move', action='store_false',help="Do Not MOVE Files")
parser.set_defaults(move=True)

# copy gps file
parser.add_argument('--copy-gps',"-g", dest='copy_gps', action='store_true',help="copy gps file")
parser.add_argument('--no-copy-gps',"-ng", dest='copy_gps', action='store_false',help="Do not copy gps file")
parser.set_defaults(copy_gps=True)

# create waypoint files
parser.add_argument('--create-waypoint',"-w", dest='create_wpt', action='store_true',help="Create waypoint")
parser.add_argument('--no-create-waypoint',"-nw", dest='create_wpt', action='store_false',help="Do not create waypoint")
parser.set_defaults(create_wpt=True)

# move over command line arguments
args = parser.parse_args()
print("*** READING FILE INFO ")
print(f"Arguments {args}")

p=args.path
save=args.save
verbose=args.debug
collaterals=args.collaterals
raw=args.raw
move=args.move
copy_gps=args.copy_gps
create_wpt=args.create_wpt

if os.path.isdir(p):
    root_path=Path(p).absolute()
    print(f"Using Path {root_path}")
else:
    root_path=Path(".").absolute()
    print(f"{p} is not a valid path, using current path {root_path}")
    sys.exit()

# fixed stuff
filetype_classes_dict=file_cleanup.FILETYPE_CLASSES_DICT
ignore_files=file_cleanup.IGNORE_FILES
gps_file="gps.jpg"
  
# delete collateral files
if collaterals:
    print("\n*** DELETING COLLATERAL FILES ")
    del_profile=file_cleanup.DELETE_PROFILE[file_cleanup.DEL_PROFILE]
    del_filetypes=del_profile["FILETYPES"]
    delete_paths=del_profile["DELETE_PATHS"]
    ignore_paths=del_profile["IGNORE_PATHS"]
    file_cleanup.delete(fp=root_path,filetype_classes_dict=filetype_classes_dict,
                              save=save, verbose=verbose,
                              ignore_files=ignore_files,ignore_paths=ignore_paths,
                              delete_paths=delete_paths,del_filetypes=del_filetypes)    

# move files
if move:
    print("\n*** MOVING FILES ")    
    ignore_paths=file_cleanup.IGNORE_PATHS
    filetype_target_folder=file_cleanup.FILETYPE_TARGET_FOLDER
    file_cleanup.move(fp=root_path,filetype_classes_dict=filetype_classes_dict,
                            save=save, verbose=verbose,
                            ignore_paths=ignore_paths,
                            ignore_files=ignore_files,
                            filetype_target_folder=filetype_target_folder)    

# delete raw files
if raw:
    print("\n*** DELETE RAW FILES ")        
    del_profile=file_cleanup.DELETE_PROFILE[file_cleanup.DEL_PROFILE_RAW] 
    del_filetypes=del_profile["FILETYPES"]
    delete_paths=del_profile["DELETE_PATHS"]
    ignore_paths=del_profile["IGNORE_PATHS"]
    file_cleanup.delete(fp=root_path,filetype_classes_dict=filetype_classes_dict,
                              save=save, verbose=verbose,
                              ignore_files=ignore_files,ignore_paths=ignore_paths,
                              delete_paths=delete_paths,del_filetypes=del_filetypes)       

# copy gps file with new timestsmp in filename  if exists
if copy_gps:
    print(f"\n*** Copy GPS File {gps_file} ")    
    file_cleanup.copy_img_file(fp=root_path,geo_file=gps_file,
                               verbose=verbose,save=save)

# create waypoints
if create_wpt:
    print("\n***************************")    
    print("*** Create waypoint files ")
    print(f"    EXIF TOOL: {CMD_EXIFTOOL}")     
    print(f"    Waypoint File: {CMD_EXIF_WAYPT_FMT}")    
    print(f"    JPG Subfolder: {JPG_FOLDER_WAYPT}")
    print(f"    Ignore Folders: {IGNORE_FOLDERS_GPX}")
 
    file_cleanup.create_gpx_waypt(fp=root_path,cmd_exif_waypt_fmt=CMD_EXIF_WAYPT_FMT,
                    exiftool=CMD_EXIFTOOL,jpg_folder_waypt=JPG_FOLDER_WAYPT,
                    ignore_folders=IGNORE_FOLDERS_GPX)                           
       