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

# path to waypoint template
# f_waypt_template=r"C:\<path to your gpx Waypoint template>"

# executables, be sure that PATHS variables are set correctly 
exe_magick = "C:/<PATH_TO>/magick.exe" # image magick
exe_exiftool= "C:/<PATH_TO>/exiftool.exe" # exiftool

# command line commands used for cmd_runner.py
p_bat=r"C:\<PATH TO YOUR COMMAND LINE FILES>"
CMD_COMMANDS={ 1:{"CMD":"<your cmd  file 1>.BAT",
                "DESC":"Description of your butt file 1"},
              2:{"CMD":"<your cmd file 2>.BAT",
                "DESC":"Description of your butt file 2"}
             }
# run a sequence of commands, number points to commands
CMD_SEQUENCE={ 1:{"COMMANDS":[1,2],
                  "DESC":"Description of Sequence 1"},
               2:{"COMMANDS":[1],
                  "DESC":"Description of Sequence 2"}
             }             

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
