""" Utility to delete files that are not part of a reference snippet file name list 
    Snippet will consider only part of a filename (the first compare_len characters)
	Use Case: Files with same prefix but different file name endings can be deleted as well, 
	even different subfolders, based on a reference list of files.
"""

import os
from os import walk
from pathlib import Path
import glob
from tools.simple_input import v

# TODO switch_to_argparse

fp = v
if not os.path.isdir(fp):
    input(f"input not a directory {fp} using current directory")
else:
    fp = os.getcwd()
	
# folder containing reference files
subpath_ref = "25Planet"
#subpath_ref = "wrongpath"
ref_path = Path(fp).joinpath(subpath_ref)
if not os.path.isdir(ref_path):
    input(f"subpath is not a directory {ref_path}")
    quit()

ref_files = []
file_list = []
# reference file type
ref_suffix_list = [".jpg"]
# types to be included as file list
suffix_list = [".jpg",".dng",".insv",".mp4",".insp",".arw",".tif",".dop"]
# exclude these folders
# exclude_folder_list = ["70POST","10RAW"]
exclude_folder_list = ["70POST"]
# length of string to be compared
compare_len = 20

for subpath_s,directories,files in os.walk(fp):
    subpath = Path(subpath_s)    
    is_exclude_folder = False
    print(f"--- {subpath_s}")
    for exclude_folder in exclude_folder_list:
        if exclude_folder in subpath.parts:
            print(f"    Folder {exclude_folder} will be excluded from analysis")
            is_exclude_folder = True
            
    for f in files:
        f_full = subpath.joinpath(f)
        f_ext = f_full.stem
        f_suffix = f_full.suffix
        if ( subpath == ref_path ) and ( f_suffix in ref_suffix_list ):
            f_prefix = f_ext[:compare_len]
            print(f"    Adding filename snippet {f_prefix}")
            ref_files.append(f_prefix)
        else:            
            if (not is_exclude_folder) and (f_suffix in suffix_list):
                file_list.append(f_full)
                print(f"    Adding file {f_ext+f_suffix}")

print("\nFILE ANALYSIS")
file_deletion_list = []
for f_full in file_list:    
    if len(ref_files) == 0:
        continue
    file_snippet = f_full.stem[:compare_len]
    if not (file_snippet in ref_files):
        print(f_full)
        file_deletion_list.append(str(f_full))

file_deletion_list.sort()                                  

print(f"\n\n########\nDELETION OF {len(file_deletion_list)} FILES \n########\n")

curr_parent = ""
for f_del in file_deletion_list:
    p_del = Path(f_del)
    if curr_parent != p_del.parent:
        curr_parent = p_del.parent
        print(f"\n--- Folder {curr_parent}")
    print("    "+p_del.stem+p_del.suffix)

delete_files = input("delete files (y)")

if delete_files == "y":
    for f_del in file_deletion_list:
        pass
        os.remove(f_del)
    print("--- files deleted! ---")

input("enter key to exit")

