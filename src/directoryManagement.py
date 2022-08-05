from os import walk

def findDirectoriesToBackup(backupDirectory: str) -> []:
    directories = []
    for (dirpath, dirnames, filenames) in walk(backupDirectory):
        directories.extend(dirnames)
        break
    return directories