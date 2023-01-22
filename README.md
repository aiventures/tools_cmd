# Command Line Tools
This repo mainly contains usages of the modules that were created in the **[tools repo](https://github.com/aiventures/tools)** for personal usage and image metadata processing.

Usage: `python <file>`, if arguments are supported, program is listed as `python <file> (--h)`

# [100] Templates

101. `argparse_template.py (--h)`\
Boilerplate template for argparse arguments. 

102. `_paths_template.py`\
Template to store paths used in scripts

103. `_paths_import_template.py`\
Template to access paths from _paths_template

104. `_paths_display.py`\
Read out path definitions from `_paths_template.py`

# [200] Image Processing 

## [201] Prerequisite
* `EXIFTOOL.exe` used for reading camera specific metadata, needs to be found in Windows path (**[EXIFTOOL](https://exiftool.org/)**)
* `IMAGEMAGICK.exe` used for resizing images, needs to be found in Windows path (**[IMAGEMAGICK](https://imagemagick.org)**)
* Some parts for reading EXIF might require Pillow (**[Installation](https://pillow.readthedocs.io/en/stable/installation.html)**) 
**NOTE** It might be necessary to define complete path ("c:/.../") to executables in in paths template.

## [220] Image Processing Preparation 

221. `img_meta_copy_meta_files.py`\
copies metadata files for image processing

222. `img_metadata_rename_files.py`\
renames copied metadata files in umo folder to be used for processing 

223. `img_move_img_manual.py`\
If image metadata doesn't contain lens information, it will be considered a manual lens and be moved to a separate folder

## [240] Image Processing Tools

241. `img_file_rename.py (--h)` (uses **[img_file_info_xls.py](https://github.com/aiventures/tools/blob/master/img_file_info_xls.py)**)\
Renames Image files based on EXIF data (supports jpg and images from panoramic cameras). 

242. `img_rename_original_filenames.py` (replaced by img_file_rename.py)\
Utility to rename original filenames (signature three letters and five digits). 
 
243. `img_rename_original_filenames_pano.py` (replaced by img_file_rename.py)\
Utility to rename original filenames:\
PANORAMA FILES\
(signature IMG_YYYYMMDD_HHMMSS_00_###_*.(filetype) )\
STANDARD OUT OF CAM FILES\
WWWDDDDD.(filetype) (three letters five digits) 

244. `img_copy_pano_metadata.py`\
 copying metadata from insp panorama files to exported image files 
 (for example taken screenshots do not contain metadata) 

245. `img_metadata_copy_from_img.py`\
copies image metadata from one source file to other files belonging to a file group 

246. `img_metadata_process_cwd.py`\
complete image metadata processing workflow

247. `img_file_info_resize_v2.py (--h)` (uses **[img_file_info_xls.py](https://github.com/aiventures/tools/blob/master/img_file_info_xls.py)**)
  * Resizes Images using IMAGEMAGICK
  * Can additionally be used to create file containing Image descriptions based on EXIF data
  
246. `img_change_metadata.py`\
If image metadata doesn't contain lens information, it will be considered a manual lens and lens image metadata (like focal length and lens model) will be added into metadata.
   
## [260] Image Collateral File Post Processing / Clean Up

261. `img_collateral_file_cleanup.py`\
Utility to delete collateral files in 1st level subfolders of a directory 

262. `img_file_info_delete_metadata.py`\
deleting metadata folder

263. `img_delete_subfolders.py`\
Deleting subfolders

264. `img_delete_pano_files.py`\
Utility to delete panorama files in a directory: check if there is a single dng file present \
(assuming the jpg or other file were deleted) gets directory from clipboard

## [280] Image Reporting Tools 

281. `img_file_info_process.py`\
saves subfolder information as json and xls

282. `img_file_info_xls_exiftool.py`\
Utility to read out important exif metadata using exiftool 

# [3] File Processing

## [310] Prerequisite

* Reading out Windows shortcuts needs `win32com` module (`pip install -U pypiwin32`)

## [320] File Processing Tools

321. `file_info.py (--h)`\
** Reads all files in given path. In case content can be read, it will be output to console (can be usefiul in combination with grep command to search for text in files). Uses **[file_module.py](https://github.com/aiventures/tools/blob/master/file_module.py)**

322. `files_delete_from_stem.py`\
Utility to delete files that are not part of a reference snippet file name list Snippet will consider only part of a filename (the first compare_len characters)\
Use Case: Files with same prefix but different file name endings can be deleted as well, even different subfolders, based on a reference list of files.
  
# [400] Other Tools

401. `video_series_rename_v2.py` (uses **[video_rename_v2.py](https://github.com/aiventures/tools/blob/master/video_rename_v2.py)**)\
Renames downloaded video files from public german tv channels downloaded with the **https://mediathekview.de** tool.\
Parses both text files and file names to check out for rename of files into series and episodes. Also generates json sidecars containing the additional data contained in the text files

402. `gpx_rename.py`\
rename gpx files according to their first occurence of track name.place this file inside directory with the gpx file (tbd)\

403. `health_data.py`\
Util file that helps to transform data from my health app into a single data frame (to be used for insert into my XLS file)