#!/usr/bin/python3
""" package for storage"""

from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
