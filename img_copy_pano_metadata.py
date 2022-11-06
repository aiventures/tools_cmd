""" copying metadata from insp panorama files to exported image files 
    (for example taken screenshots do not contain metadata)
"""
import _paths as img_paths
from tools import img_file_info_xls as img_info
from tools_cmd._paths import p_umo_photos as fp_root

# TODO switch_to_argparse

max_level=1
exiftool="exiftool.exe"
verbose=True
save=True
prompt=True
software="Insta360 one x2"
pano_filetypes=["insp"]
jpg_filetypes=img_info.TYPE_JPG

exiftool_cmds=img_info.copy_metadata_from_panofile(fp_root,exiftool=exiftool,
                                verbose=verbose,save=save,max_level=max_level,
                                prompt=prompt,software=software,
                                pano_filetypes=pano_filetypes,
                                jpg_filetypes=jpg_filetypes)