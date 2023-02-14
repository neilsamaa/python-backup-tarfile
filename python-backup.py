import os
import tarfile
from pathlib import Path
from datetime import datetime

# name of the backup file
FILENAME='backup'
# max number of backup file (will be deleted if more than set)
MAX_BACKUP_FILE = 2
# directory to save the backup
BACKUP_DIRECTORY='/home/mirza/backup' # Auto create new directory if path doesn't exist
# directory you want to backup
OBJECT_TO_BACKUP='/home/mirza/folder'

BACKUP_FILENAME = FILENAME.replace(" ","_")
DATE=datetime.now().strftime("%Y-%m-%d-%H%M%S")
files = tarfile.open(f'{BACKUP_DIRECTORY}/{BACKUP_FILENAME}_{DATE}.tar.gz', 'w:gz')

def tarfile():
    files.add(OBJECT_TO_BACKUP, arcname=os.path.basename(OBJECT_TO_BACKUP)) 
    for file in files.getnames():
        print ("added files %s" % file)
    files.close()

def finish():
    print('Backup done!')
    print(f'File {BACKUP_FILENAME}_{DATE}.tar.gz saved at {BACKUP_DIRECTORY}')

backup_directory_path = Path(BACKUP_DIRECTORY)

if backup_directory_path.exists():
    print('Backup started...')
    tarfile()
    finish()
else:
    print('Backup path not found...')
    print('New directory created...')
    print('Backup started...')
    backup_directory_path.mkdir(parents=True, exist_ok=True)
    tarfile()
    finish()

existing_backups = [
    x for x in backup_directory_path.iterdir()
    if x.is_file() and x.suffix == '.gz' and x.name.startswith(BACKUP_FILENAME)]

oldest_to_newest_backup_by_name = list(sorted(existing_backups, key=lambda f: f.name))
if len(oldest_to_newest_backup_by_name) > MAX_BACKUP_FILE:
    print("The backup file has exceeded the set limit, old files will be replaced!")
    while len(oldest_to_newest_backup_by_name) > MAX_BACKUP_FILE:
        backup_to_delete = oldest_to_newest_backup_by_name.pop(0)
        backup_to_delete.unlink()