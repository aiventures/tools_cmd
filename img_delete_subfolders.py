from tools import img_file_info_xls as img_info
from tools_cmd._paths import p_umo_photos as fp

# deleting subfolders       
# TODO switch_to_argparse

verbose=False
delete_folder_list=["metadata"]
prompt=True
delete=True
del_folders=img_info.delete_subfolders(fp,verbose=False,delete_folder_list=delete_folder_list,
                                       prompt=prompt,delete=delete)