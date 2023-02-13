
# Python Backup Script Tarfile

This script allows you to backup a file or folder as a tar file into a backup folder. It is designed to be run periodically for backing up something like an SQLite database. It can run automatically with specific time for backup using cronjob.

**Tape Archive Files** is what the letter TAR in tar files stands for. Tar files are the archive files which allows you to store numerous files in a single file. Open-source software is distributed using tar files. Tar files typically end in.tar, but after they've been compressed using tools like gzip, they have the ending tar.gz.



## Various file modes to open Python tar file

| Parameter | Description |
| :-------- | :-----------|
| `r`      | reads a TAR file by opening it. |
| `r`      | Reads an uncompressed TAR file when it is opened. |
| `w or w`      | Opens a TAR file for uncompressed writing |
| `a or a`      | Opens a TAR file for appending without compression. |
| `r:gz`      | opens a TAR file that has been compressed with gzip for reading. |
| `w:gz`      | opens a TAR file that has been compressed with gzip for writing. |
| `r:bz2`      | opens a TAR file with bzip2 compression for reading. |
| `w:bz2`      | opens a TAR file with bzip2 compression for writing. |

## Creating a tar file using Python
Using the tarfile module in Python, tar files can be produced. Add more files to the tar file after opening a file in write mode.

## Using open() method
An example of Python code that creates a tar file is shown below. Here, we create a tar file using the open() method .The open() method here accepts "w" to open the file in write mode along with the filename of the tar file that will be produced as its first parameter.

## Example
Following is an example to create a tar file using open() method −

```Python
#importing the module
import tarfile

#declaring the filename
name_of_file= "TutorialsPoint.tar"

#opening the file in write mode
file= tarfile.open(name_of_file,"w")

#closing the file
file.close()
```
## Output
As an output we can see a tar file created with the name “TutorialsPoint”.
