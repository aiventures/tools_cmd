""" import variables from another python program """

import _paths as img_paths

# alternatively use direct import
# from tools_cmd._paths import p_umo_photos

# import set of expected variables programmatically
imported_vars=["p_umo_photos","p_photos_transient","p_photos_meta"]
iv=[]
for k,v in img_paths.get_variables(imported_vars).items():
    iv.append(k)
    globals()[k] = v
print(f"IMPORTED VARIABLES: {', '.join(iv)}")



