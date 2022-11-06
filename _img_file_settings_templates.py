""" file with personal settings rename this to _img_file_settings.py
    this file is used for variable import for img_file_cleanup.py
    and for using img_file_validator.py
    COPY THIS FILE AND SAVE IT AS _img_file_settings.py in your executable path
"""

# setup file, folder structure for a woring setup is described below (P_... is a folder)
# P_EXIFTOOL
#         +---  exiftool.exe       [CMD_EXIFTOOL] (Location of EXIFTOOL Executable / It is advisable to extend PATH so that exiftool can be directly called ) 
# P_CONTROL                        (FOLDER CONTAINING CONTROL FILES that will be reused)
#         +---  metadata.tpl       [FP_METADATA_TPL] (Control File Template will be copied over when using image file validator, Prefill the template file with your own 
#                                   settings. Variables defined here / check the template file for documentation:
#                                    ['EXIFTOOL_FILE','META_PROFILES_FILE','META_FILE', 'GPX_FILE', 'WAYPOINT_FILE',
#                                    'KEYWORD_HIER_FILE', 'CALIB_IMG_FILE', 'XCALIB_OFFSET', 'DEFAULT_LATLON_FILE',
#                                    'WORK_DIR', 'IMG_EXTENSIONS', 'TECH_KEYWORDS', 'OVERWRITE_KEYWORD', 'OVERWRITE_META',
#                                    'COPYRIGHT', 'COPYRIGHT_NOTICE', 'INFO_CREDIT', 'CREDIT',
#                                    'SOURCE', 'CREATE_GEO_METADATA', 'CALIB_DATETIME', 'TIMEZONE',
#                                    'DEFAULT_LATLON', 'CREATE_LATLON', 'CREATE_DEFAULT_LATLON', 'DEFAULT_MAP_DETAIL',
#                                    'DEFAULT_GPS_EXT', 'GPS_READ_REMOTE']
#         +---  exiftool_wpt.fmt    [CMD_EXIF_WAYPT_FMT] (Exiftool Waypoint Transformation file - see above )
#         +---  metadata_exif_keywords.json 
#         +---   
#
# For Geotagging, you either may use a complete GPX Track to individually Tag each image or your can only work 
# by copying/ placing a Open Street Map url link into the photo folder (=Each folder will be tagged with this geolocation)
# [P_PHOTOS_ROOT]                    (PHOTOS ROOT FOLDER)
#             +--- PHOTO_SUBFOLDER (usually named YYYYMMDD_FOLDERNAME, image files to be placed here)
#                                +--- geo.jpg [CALIB_IMG_FILE] (calibration image of GPS screenshot containing Camera DateCreated Timestamp)       
#                                +--- gps.gpx [GPX_FILE] (GPS Track)       
#                                +--- gps_wpt.gpx [CMD_EXIF_WAYPT_FMT] (GPS Waypoints / Create a Waypoint with your GPS when you take geo.jpg)       
#                                +--- metadata.tpl [F_METADATA] (Control File containing all links to create Geotagged images / is copied from [P_CONTROL]
#                                                                and will be enriched with additional metadata)       
#                                +--- metadata_exif.tpl [META_FILE] (File Containing EXIF keywords / will be created with img_file_validator and the use of 
#                                                           metadata_exif_keywords.json)       
#                                +--- default.geo [DEFAULT_LATLON_FILE] (File Containing Reverse Geolocation Information for Calibration waypoint )       
#                                +--- YYYYMMDD_FOLDERNAME_gps_images_wpt.gpx (GPS Waypoints created from geotagged images, after images were geotagged)       
#                                +--- <any osm link>.url (the 1st found OSM Link will be parsed (https://www.openstreetmap.org/#map=<DETAIL>/<LAT>/<LON>) 
#                                                           and Coordinates will be extracted  ). File name is irrelevant :-)
#                                +--- 70POST  [JPG_FOLDER_WAYPT] (Folder)
#                                          +--- YYYYMMDD_HHMMSS_gps.jpg (when a gps.jpg file is found, a copy with the creation 
#                                                                        datetime in folder name will be created for convenience)
#                                +--- <other subfolders>
#                                +--- <ignore  subfolders> [IGNORE_FOLDERS_GPX]  (these folders will be excluded from processing)

# ignore image folders when creating waypoint files
IGNORE_FOLDERS_GPX=["IGNORE_FOLDER1","IGNORE_FOLDER2"]
# folder location of format file 
# https://exiftool.org/geotag.html
# https://github.com/exiftool/exiftool/blob/master/fmt_files/gpx_wpt.fmt
CMD_EXIF_WAYPT_FMT=r'C:/< _TODO_ your path to P_CONTROL>/exiftool_wpt.fmt'
# Subfolder used for creating waypoint files / I use 70POST
JPG_FOLDER_WAYPT="70POST"
# location of exiftool if in path it is exiftool
CMD_EXIFTOOL="<_TODO_ P_EXIFTOOL>/exiftool.exe"
# file path of Control File Template this takes the form 
FP_METADATA_TPL=r"C:/< _TODO_ your path to P_CONTROL>/metadata.tpl"
# metadata file names / all will be collected in metadata.tpl
F_METADATA="metadata.tpl"
# root folder for photos, structure and files / Variables in Brackets correspond to variables defined here and in control file metadata.tpl
P_PHOTOS_ROOT=r"C:/< _TODO_ your path to P_PHOTOS_ROOT>"

# HOME LATLON COORDINATES / used for calculating distance to your gps start location
LATLON_HOME=[52.5143,13.3502]
