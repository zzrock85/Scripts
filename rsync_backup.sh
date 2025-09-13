#!/bin/bash
# This script synchronizes the contents of /Volumes/Backup_1/Zdjęcia_Video/ to /Volumes/Backup_2/Zdjęcia_Video/
# using rsync with archive mode, verbose output, human-readable numbers,
# and deletes files in the destination that are no longer present in the source.
rsync -avh --delete /Volumes/Backup_1/Zdjęcia_Video/ /Volumes/Backup_2/Zdjęcia_Video/