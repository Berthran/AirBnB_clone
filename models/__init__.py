#!/usr/bin/python3
'''
This file is used to initialize the models package.
'''

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage to access stored instances
storage = FileStorage()
# Get all instances stored in a file specified in FileStorage Class
storage.reload()
