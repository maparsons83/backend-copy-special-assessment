#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse
from pprint import pprint
from zipfile import ZipFile

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(directory):
    dir_list = os.listdir(directory)
    ab_path = []
    for file in dir_list:
        special = re.findall(r'__\w+__', file)
        if special: 
            ab_path.append(os.path.abspath(file))
    return ab_path

def copy_to(paths, directory):
    for path in paths:
        shutil.copy(path, directory)

def zip_to(paths, zippath):
    cmd = 'zip -j {} '.format(zippath) + ' '.join(paths)
    status, output = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(status)
    

def main(args=None):
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='returns special files from given directory')
    # TODO need an argument to pick up 'from_dir'
    results = parser.parse_args(args)
    todir = results.todir
    from_dir = results.from_dir
    tozip = results.tozip

    if not results:
        print parser.usage()
        sys.exit(1)
    if not from_dir:
        print("Please provide a directory to read from")
        print parser.usage()
        sys.exit(1)
    special_paths = get_special_paths(from_dir)
    if todir:
        copy_to(special_paths, todir)
    elif tozip:
        zip_to(special_paths, tozip)
    else: 
        print(special_paths)
    


    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
  
if __name__ == "__main__":
    main()

    
