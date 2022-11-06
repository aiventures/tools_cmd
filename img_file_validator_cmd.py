""" Sample program to process metadata with file validator 
    Also check out the instructions here
    https://github.com/aiventures/tools/blob/master/img_file_validator_templates/readme..md
"""
from importlib import reload
# copy _img_file_settings_tmplate.py and adjust variables accordingly 
from tools_cmd import _img_file_settings as fs

from tools.img_file_validator import ImageFileValidator
img_validator = ImageFileValidator(
                                    p_photos_root=fs.P_PHOTOS_ROOT,
                                    ignore_folders=fs.IGNORE_FOLDERS_GPX,
                                    exif_tool=fs.CMD_EXIFTOOL,
                                    cmd_exif_waypt_fmt=fs.CMD_EXIF_WAYPT_FMT,
                                    jpg_folder_waypt=fs.JPG_FOLDER_WAYPT,
                                    fp_metadata_tpl=fs.FP_METADATA_TPL,
                                    f_metadata=fs.F_METADATA,
                                    latlon_home=fs.LATLON_HOME
                                   )
# Check / Execute Consolidation of metadata
img_validator.consolidate_control_data()
# Display file actions
if input("Display File Actions (y)? ")=="y":
    img_validator.display_file_actions()