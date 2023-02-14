
# Python Backup Script Tarfile

This script allows you to backup a file or folder as a tar file into a backup folder. It is designed to be run periodically for backing up something like an SQLite database. It can run automatically with specific time for backup using cronjob.

**Tape Archive Files** is what the letter TAR in tar files stands for. Tar files are the archive files which allows you to store numerous files in a single file. Open-source software is distributed using tar files. Tar files typically end in.tar, but after they've been compressed using tools like gzip, they have the ending tar.gz.


## Initialize Variable
Before running script you need to initialize this according to your needs. 
```Python
# name of the backup file
FILENAME='backup'
# max number of backup file (will be deleted if more than set)
MAX_BACKUP_FILE = 2
# directory to save the backup
BACKUP_DIRECTORY='/home/mirza/backup' # Auto create new directory if path doesn't exist
# directory you want to backup
OBJECT_TO_BACKUP='/home/mirza/folder'
```

## Various file modes to open Python tar file
In this script Python code that creates a .tar.gz file is shown below. Here create a .tar.gz file using the open() method .The open() method here accepts "w:gz" to open the file in write mode along with the filename of the .tar.gz file that will be produced as its first parameter. You can change file format .tar and others depending various modes below.

| Parameter | Description |
| :-------- | :-----------|
| `r`      | reads a TAR file by opening it. |
| `r`      | reads an uncompressed TAR file when it is opened. |
| `w or w`      | opens a TAR file for uncompressed writing. |
| `a or a`      | opens a TAR file for appending without compression. |
| `r:gz`      | opens a TAR file that has been compressed with gzip for reading. |
| `w:gz`      | opens a TAR file that has been compressed with gzip for writing. |
| `r:bz2`      | opens a TAR file with bzip2 compression for reading. |
| `w:bz2`      | opens a TAR file with bzip2 compression for writing. |

```Python
files = tarfile.open(f'{BACKUP_DIRECTORY}/{BACKUP_FILENAME}_{DATE}.tar.gz', 'w:gz')
```

## Backuping
This script below build a .tar.gz (aka .tgz) for an entire directory tree.
This will create a gzipped tar archive containing a single top-level folder with the same name and contents as `OBJECT_TO_BACKUP`.
```Python
def tarfile():
    files.add(OBJECT_TO_BACKUP, arcname=os.path.basename(OBJECT_TO_BACKUP)) 
    for file in files.getnames():
        print ("added files %s" % file)
    files.close()
```

Using `arcname=os.path.basename(OBJECT_TO_BACKUP)` still means that the archive contains a folder which contains the contents of OBJECT_TO_BACKUP. If you want the root of the archive to contain the contents themselves, and not contents within a folder, use `arcname=os.path.sep` instead like script below.
```Python
def tarfile():
    files.add(OBJECT_TO_BACKUP, arcname=os.path.sep) 
    for file in files.getnames():
        print ("added files %s" % file)
    files.close()
```
