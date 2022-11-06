""" Utility to delete panorama files in a directory:
    check if there is a single dng file present 
    (assuming the jpg or other file were deleted)
    gets directory from clipboard
"""

import os
from tools.simple_input import v
from image_meta.persistence import Persistence as ps

# TODO switch_to_argparse

fp = v
if not os.path.isdir(fp):
    fp=os.getcwd()
    print(f"Using current directory: {fp}")

# regex for filegroup pattern: 1st 19 Characters
r_group = "^(.{1,19})"
file_group_regex_list = [r_group]
print(f"REGEX FOR FILEGROUPS: {file_group_regex_list}")

# either all or any regexes so that file name matches pattern
# in this case only one entry
file_group_match_type="ALL"

# regex to filter files in resulting file groups
# here we want to check whther we have dng files
r_file = ".*(dng)$"
file_regex_list = [r_file]
print(f"REGEX FOR FILE SIGNATURE: {file_regex_list}")

# file check to fit ALL or ANY regexes given in file_regex_list
file_match_type="ANY"
# either ANY or ALL files in a file group need to match 
file_group_match_type_analyze="ANY"

# Only add a file match when a file matches to criteria for first occurence
# Avoids double listing of file paths in result list
file_group_single_match=True

# display info
show_info=False

fa=ps.group_and_analyze_files( fp, file_group_regex_list,
                            file_group_match_type=file_group_match_type,
                            file_regex_list=file_regex_list,
                            file_match_type=file_match_type,
                            file_group_match_type_analyze=file_group_match_type_analyze,
                            file_group_single_match=file_group_single_match,
                            show_info=show_info )

# in our case we want to delete occurences of file groups having only one file

f_deletion_list = []

for file_group,file_info in fa.items():
    file_matches = file_info["file_match_dict"]
    files = list(file_matches.keys())
    file_num = file_info["num_files"]    
    print(f"-- File Group: {file_group}, {file_num} files")
    if file_num == 1 and file_matches[files[0]]:
            print(f"   Single File in Group, delete: {files}")
            f_deletion_list.extend(files)

print(f"\nDeletion list: {f_deletion_list}\n")

if f_deletion_list and input("Do You Want To Delete?") == 'y':
    for f in f_deletion_list:
        print(f"   Deleting: {f}")
        os.remove(f)        
else:
    print("Abort, No Files / Files not deleted")    
	
input("enter key to exit")

