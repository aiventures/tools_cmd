""" extracts table of contents from a markdown file 
    intregrate into bash using 
    alias py_md2toc='python "${p_tools_cmd}/md2toc_cmd.py" -f'
"""

import sys
import argparse
from pathlib import Path
import os
from tools import file_module as fm

parser = argparse.ArgumentParser()
parser.add_argument("--file","-f",default="./sample/mdtoc.md",help="Markdown File Name",metavar='Markdown File Name')
parser.add_argument('--save',"-c", dest='save', action='store_true',help="Save TOC to file (<orig_file_name>_toc.md)")
parser.add_argument('--no-save',"-nc", dest='save', action='store_false',help="Do not save TOC")
parser.set_defaults(save=True)

args = parser.parse_args()
print("*** Generating Table of Contents ")
print(f"Arguments {args}")

f=args.file
save=args.save

if os.path.isfile(f):
    file_path=Path(str(Path(f).absolute()))
    print(f"Using File {file_path}")
else:
    print(f"ERROR: {f} is not a valid path")
    sys.exit()

orig_path=os.getcwd()
file_mdtoc=file_path.stem+"_toc.md"
print(file_mdtoc)
os.chdir(file_path.parent)

s_toc=fm.md2toc(file_path.name,as_string=True)
print(s_toc)

if save:    
    fm.save_txt_file(file_mdtoc, s_toc)
    print(f"Saved TOC to {file_mdtoc}")

os.chdir(orig_path)

