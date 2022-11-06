""" Sample program for DuplicatesFile Class """
import sys
import os
import traceback
from datetime import datetime
from image_meta.persistence import Persistence

# TODO switch_to_argparse

# specify locations / filepaths to check
fp_list = [r"I:",r"R:"] 

s = "D:\<>"
p = r"C:<>\filelist.txt"

# note p needs to be file with extension otherwise you'll get a [ERRNO 13]
# use regex expressions to filter out specific files 
# (example: mp4 files containing doc in absolute path name)
filter_list = ["mp3"]
filter_list= None

# regex expression to exclude files from filtered list
# (example: exclude files that contain ignore_folder in 
# absolute path name)
exclude_list = None
# delete marker to display files for deletion
delete_marker=None
# Only display files for deletion
show_del_files_only=False
# debug mode: show additional processing info
show_info = False
# also show link for url files
show_url=True
# start numbering index (if set To None only hypens will be shown)
start_number = 1
# only display filename instead alongside with change date / file size
show_filename_simple = False
# sort files per folder by date in ascending-descending order
# otherwise it will be shown alphabetically
sort_by_date=True
reverse=True

# method to display results, output will be rerouted to file and displayed
# (internally calls read_duplicate_files method)        
print(f"write output to > {p}")
sys.stdout=open(p,"w")
d=Persistence.display_file_list_by_folder(fp_list,ignore_paths=exclude_list,files_filter=filter_list,
                delete_marker=delete_marker, show_del_files_only=show_del_files_only,
                show_info=show_info,show_url=show_url, start_number=start_number,
                show_filename_simple=show_filename_simple,sort_by_date=sort_by_date,reverse=reverse)
if isinstance(fp_list,str):
    print(f"- Path: {fp_list}")  
elif isinstance(fp_list,list):
    for fp in fp_list:
        print(f"- Path: {fp}")                
sys.stdout.close()                       

# open file in default txt editor (win only)
if os.path.isfile(p):
    os.system(f'start {os.path.realpath(p)}')
else:
    input(f"--- file {p} not found press key to continue ---")
