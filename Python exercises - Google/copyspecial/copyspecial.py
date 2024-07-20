#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess
import zipfile

"""Copy Special exercise
"""


# Write functions and modify main() to call them
def get_special_paths(foldername):
  result = []
   # list of paths in that dir
  paths = os.listdir(foldername) 
  for fname in paths:
    match = re.search(r'__(\w+)__', fname)
    if match:
      result.append(os.path.abspath(os.path.join(foldername, fname)))
  return result


def copy_to(pathslist, cpydirectory):
  if not os.path.exists(cpydirectory):
    os.mkdir(cpydirectory)
  for path in pathslist:
    fname = os.path.basename(path)
    shutil.copy(path, os.path.join(cpydirectory, fname))
    # could error out if already exists os.path.exists():



def zip_to(paths, zipfile_name):
  # using python builtin zipfile module
    print("Creating zip file:", zipfile_name)
    with zipfile.ZipFile(zipfile_name, 'w') as myzip:
        for path in paths:
            myzip.write(path, os.path.basename(path))
    print("Zip file created successfully:", zipfile_name)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)
    
  # Call your functions
  pathslist = []
  for dirname in args:
    pathslist += get_special_paths(dirname)

  if todir:
    copy_to(pathslist, todir)
  elif tozip:
    zip_to(pathslist, tozip)
  else:
    print('\n'.join(pathslist))
  # LAB(end solution)

if __name__ == '__main__':
  main()
