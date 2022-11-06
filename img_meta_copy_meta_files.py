from image_meta.persistence import Persistence
from tools_cmd._paths import p_umo_photos as fp
from tools_cmd._paths import p_photos_meta as fp_src

#import atexit
#atexit.register(input, 'Press Enter to continue...')

# TODO switch_to_argparse

print("*** Copy Metadata Files / Process Coordinates ***")

METADATA = "metadata.tpl"
files_copy = ["metadata_exif.tpl",METADATA]
save = True
showinfo = True

finished = Persistence.copy_meta_files(fp=fp,fp_src=fp_src,metadata=METADATA,files_copy=files_copy,save=save,showinfo=showinfo)
input(f"Processing Finished; {finished}, hit key to exit")
########################