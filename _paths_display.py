""" import variables from another python program """

import _paths as img_paths

# p_umo_photos=r"C:\<path to your own new photos>"
# p_photos_transient=r"C:\<path to your own photos intermediate storage location>"
# p_photos_meta=r"C:\<path to your photo metadata>"
# p_dict

# testing
imported_keys = list(img_paths.__dict__.keys())
print("**** Imported Variables from module  _paths")
[print(f"    * {k} : {img_paths.__dict__[k]}") for k in imported_keys if not k.startswith("__")]

# check for imported variables
imported_vars=["p_umo_photos","p_photos_transient","p_photos_meta","p_dict"]

for imported_var in imported_vars:
    value=img_paths.__dict__.get(imported_var,None)
    if value:
        globals()[imported_var] = value
    else:
        print(f"#### Param {imported_var} not found, check _paths.py")
    
print("     IMPORTED VARIABLES")
print([{v:eval(v)} for v in dir() if v.startswith("p_")])

