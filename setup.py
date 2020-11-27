import sys
import os
from cx_Freeze import setup, Executable

VERSION = "0.2.2"

include_files = ["client\\certs", "client\\resource"]

path = sys.path
path[0] += "\\client"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"include_files": include_files,
                     "path": path}

exe = Executable(script='client\\client.py') # , icon='pepega.png')

setup(name="Чач",
      version=VERSION,
      description="Чач для ощения",
      options={"build_exe": build_exe_options},
      executables=[exe])
