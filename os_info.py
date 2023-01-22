""" displays some os information """
import os
import sys
import site

if __name__ == "__main__":
    # https://docs.python.org/3/library/os.html
    for k in os.environ.keys():
        print(f"{k:<30}: {os.getenv(k)}")
    # https://docs.python.org/3/library/sys.html
    print(f"{'os.getlogin':<30}: {os.getlogin()}")
    print(f"{'os.getcwd':<30}: {os.getcwd()}")

    print(f"{'os.get_exec_path':<30}: {os.get_exec_path()}")
    print(f"{'sys.path':<30}: {sys.path}")
    print(f"{'sys.base_exec_prefix':<30}: {sys.base_exec_prefix}")
    try: print(f"{'sys.base_prefix':<3py-}: {sys.base_prefix}")
    except: pass
    try: print(f"{'sys.executable':<30}: {sys.executable}")
    except: pass
    print(f"{'sys.getdefaultencoding':<30}: {sys.getdefaultencoding()}")
    print(f"{'sys.getfilesystemencoding':<30}: {sys.getfilesystemencoding()}")
    print(f"{'sys.modules':<30}: {list(sys.modules.keys())}")
    print(f"{'sys.platform':<30}: {sys.platform}")
    print(f"{'sys.platlibdir':<30}: {sys.platlibdir}")
    print(f"{'sys.prefix':<30}: {sys.prefix}")
    print(f"{'sys.version':<30}: {sys.version}")
    print(f"{'sys.version_info':<30}: {sys.version_info}")
    print(f"{'sys.winver':<30}: {sys.winver}")
    print(f"{'site.getsitepackages':<30}: {site.getsitepackages()}")

