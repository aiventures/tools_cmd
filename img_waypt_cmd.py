""" changes metadata for given path / file """

import sys
import argparse
from pathlib import Path
import os
from _paths import f_waypt_template
from tools import img_waypt

parser = argparse.ArgumentParser()
parser.add_argument("--path","-p",default=".",help="StartPath",metavar='File Path')

parser.add_argument("--exiftool","-et",default="exiftool.exe",help="Exiftool Executable",metavar='Exiftool Executable')
parser.add_argument("--timezone","-tz",default="Europe/Berlin",help="Timezone",metavar='Timezone')
parser.add_argument("--waypt_tpl","-wpt",default=f_waypt_template,help="Waypoint Template File",metavar="Waypoint Template File")
parser.add_argument("--gpx_trk","-g",default="gps.gpx",help="GPX Track Name",metavar="GPX Track Name")
parser.add_argument("--gpx_img","-i",default="gps.arw",help="Image Containing GPX Calibration Date",metavar="GPX Track Name")
parser.add_argument("--time","-t",default=None,help="Time as read from GPS Calibration Image (HH:MM:SS)",metavar="GPS Calibration Date")
parser.add_argument("--waypt_file","-f",default="gps_wpt.gpx",help="Name of Waypoint File",metavar="Waypoint File Name")

args = parser.parse_args()
print(f"Arguments {args}")
p=args.path
exiftool=args.exiftool
tz=args.timezone
waypt_tpl=args.waypt_tpl
gpx_trk=args.gpx_trk
gpx_img=args.gpx_img
time_s=args.time
waypt_file=args.waypt_file

if os.path.isdir(p):
    p=str(Path(p).absolute())
    print(f"Using Path {p}")
else:
    print(f"{p} is not a valid path")
    sys.exit()
    
# create full paths 
gpx_trk = os.path.join(p,gpx_trk)
gpx_img = os.path.join(p,gpx_img)

img_waypt.create_wpt_file(f_img=gpx_img,f_gpx=gpx_trk,
                          time_gps=time_s,
                          f_waypt_template=waypt_tpl,tz=tz,
                          f_wpt=waypt_file,exiftool=exiftool)

