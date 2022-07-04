import os
import shutil
from setuptools import sandbox

# Build DSCSRenderer and move artefacts to CWD
os.chdir("libs")
os.chdir("DSCSRenderer")
os.system("python setup.py build_ext --inplace")
os.chdir("..")
os.chdir("..")

pkg_path = os.path.join("libs", "DSCSRenderer", "dist")
for file in os.listdir(pkg_path):
    dest_path = os.path.join(".", file)
    if os.path.exists(dest_path):
        os.remove(dest_path)
    shutil.move(os.path.join(pkg_path, file), dest_path)
