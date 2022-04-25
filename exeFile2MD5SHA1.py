#coding=UTF-8
# XingHe Studio File to MD5 and SHA1 (Compile App)
# 星河创作室(XingHeStudio.com)
# Create by Stream.Wang 2012-04-10
# Modify by Stream.Wang 2012-08-19

from distutils.core import setup
import py2exe,sys
sys.path.append(r"s:\Development\Python\Python.XHLib")

setup(
    version = "1.0.0.20120819",
    description = "XingHe Studio File to MD5 and SHA1",
    name = r"pyFile2MD5SHA1",
    options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "ascii": 0,
                          "bundle_files": 1}},
    zipfile = None,
    # targets to build
    console = [{"script": r"pyFile2MD5SHA1.py", "icon_resources": [(1, r"pyFile2MD5SHA1.ico")]} ]
    )



