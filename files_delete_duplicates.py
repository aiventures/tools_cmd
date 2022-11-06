import os
from image_meta.persistence import Persistence 

# TODO switch_to_argparse

fps = ["I:\\","R:\\"]
ignore_paths = ["kopiert","android"]
files_filter = ["mp4"]

delete_all_duplicates = True
delete_folder = True
delete_marker = "cleanup.txt"
delete_ext = ["mp4","txt"]

show_info = True
verbose = False
persist = False

# first only show files for deletion
Persistence.delete_files_mult(fps,ignore_paths=ignore_paths,files_filter=files_filter,
                              delete_marker=delete_marker,delete_all_duplicates = delete_all_duplicates, 
                              delete_folder=delete_folder,delete_ext = delete_ext,
                              persist=False,show_info=show_info,verbose=verbose)
                              
ans = input("\nDELETE FILES (y/n): ")
if ans.lower() == "y":
    Persistence.delete_files_mult(fps,ignore_paths=ignore_paths,files_filter=files_filter,
                                  delete_marker=delete_marker,delete_all_duplicates = delete_all_duplicates, 
                                  delete_folder=delete_folder,delete_ext = delete_ext,
                                  persist=True,show_info=False)
    input("-- Deletion done, enter key to exit ---")    
else:
    input("Deletion skipped, enter key to exit")
                             