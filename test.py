# Scan Filesystem and Return all large directories and large files
# select files/directories from list to delete
# delete selected files/directories
# mark selected files/directories to never be deleted

from pathlib import *

current_dir = Path.cwd()
home_dir = Path.home()


# path.stat().st_size will return size of file
# path.is_dir() returns true if its a directory, false if not or if doesnt exist
# path.is_file() returns true if its a file, false if not or if it doesnt exist
# path.unlink() removes file
# path.rmdir() removes directory if empty


#Cleanse file list making sure not to display critical files
foundFiles = [x for x in allFiles if x not in criticalFiles]
#format files with name and size
formattedFiles = []
for x in foundFiles:
    fileTuple = (x, Path.stat(x).st_size) #should return (file name, file size)
    formattedFiles.append(fileTuple) #add the reformatted file object to the list of formatted files to then be sorted
    
#Sort files and return the 20 largest files
def sortFiles(formattedFiles): 
    return(sorted(formattedFiles, key = lambda x: x[1], reverse=True))

#Full list
sortedFileList = sortFiles(foundFiles) #use case: show all 
#Short normal list
largestFiles = sortFiles(foundFiles)[0:20] #used the majority of the time

print(largestFiles)

