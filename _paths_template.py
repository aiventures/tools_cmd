""" define image main folders to be used for scripts in this folder """

# define your own root paths here and rename this template to _paths.py

# That's how my images are organized
# <ROOT_IMAGE_FOLDER>
# +-- <p_photos_meta> (folder containing processing files, like metadata / gfeo metadata files)
# +-- <p_umo_photos> (unprocessed images)
#      +--  <image_folder>
#           +--  <meta_folder>
#           +--  <raw image folder>
#           +--  <post process / final image folder>
#   ...
# +-- <p_photos_transient> (processed images, waiting to be put into archive)
#     +-- (like above)

# folder location: root for all unprocessed folders containing images
p_umo_photos=r"C:\<path to your own new photos>"
p_photos_transient=r"C:\<path to your own photos intermediate storage location>"
p_photos_meta=r"C:\<path to your photo metadata>"

# alternatively in your own script, diurectly import variable using
# from tools_cmd._paths import p_umo_photos as fp

def get_variables(variable_list):
    """ returns requested variables from globals """
    out={}
    variables = globals()
    for k in variable_list:
        v = variables.get(k,None)
        if v:
            out[k]=v
    return out
