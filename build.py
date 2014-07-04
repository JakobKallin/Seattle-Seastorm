# This file is part of Seastorm
# Copyright 2014 Jakob Kallin

import os.path
import shutil
import sys
import zipfile

def addToArchive(path, archive):
  if os.path.isfile(path):
    if not path.endswith('.pyc'):
      archive.write(path)
  elif os.path.isdir(path):
    for filename in os.listdir(path):
      addToArchive(os.path.join(path, filename), archive)

def addFolderToArchive(folder, archive):
  for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if os.path.isfile(path):
      archive.write(path)
    elif os.path.isdir(path):
      addFolderToArchive(path, archive)

if len(sys.argv) < 3:
  print 'Usage: build.py output_path cors_origin'
else:
  outputPath = sys.argv[1]
  corsOrigin = sys.argv[2]
  
  # Copy all the client files into the output path, which is where they should
  # be served from. If the output directory already exists, remove it if empty
  # so that the user doesn't have to remove it manually.
  if os.path.exists(outputPath):
    if not os.path.isdir(outputPath):
      print 'output_path is not a directory'
      sys.exit(1)
    elif len(os.listdir(outputPath)) > 0:
      print 'output_path is not empty'
      sys.exit(1)
    else:
      os.rmdir(outputPath)

  shutil.copytree('client', outputPath)
  
  # Copy all of the server files into a ZIP file.
  archive = zipfile.ZipFile(os.path.join(outputPath, 'seastorm.zip'), 'w')
  os.chdir('server')
  for filename in os.listdir('.'):
    if not filename == 'tests':
      addToArchive(filename, archive)
  os.chdir('..')
  
  # Include a text file containing the CORS origin, so that the server can
  # send the correct headers.
  archive.writestr('origin', corsOrigin)
  
  archive.close()