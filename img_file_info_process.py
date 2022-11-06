import pprint
from pathlib import Path
import tools.img_file_info_xls as im_info
from tools_cmd._paths import p_umo_photos as fp

fn = "img_file_info"
p_root=Path(fp)
fp_xls = str(Path.joinpath(p_root,fn+".xls"))
fp_json = str(Path.joinpath(p_root,fn+".json"))
subpath_info_dict=im_info.get_subpath_info_dict(fp)
# use pretty printer
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(subpath_info_dict)
im_info.save_subpath_info_dict(subpath_info_dict,fp_json,fp_xls)