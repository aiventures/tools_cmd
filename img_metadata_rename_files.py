import os
from image_meta.persistence import Persistence
import _paths as img_paths
from tools_cmd._paths import p_umo_photos as fp

print("*** Rename metadata Files ***")

save = True

for subpath,subdirs,files in os.walk(fp):
    # get aboslute path
    for f in files:
        f_absolute=os.path.join(subpath,f)        
        f_default_file=os.path.join(subpath,"metadata_exif.tpl")
        # only consider metadata files
        if f.startswith("metadata_exif_") and f.endswith(".tpl"):
            print(f"RENAME {f_absolute}")
            # if there is already a default file, remove it
            if os.path.isfile(f_default_file):
                print(f" removing {f_default_file}")
                if save:
                    os.remove(f_default_file)
            # rename found file
            if save:
                os.rename(f_absolute,f_default_file)
print("*** END Rename metadata Files ***")                