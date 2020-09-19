#Compare file names and file sizes of files inside an original directory with file names and file sizes inside a destination directory.
#Write name of script, discs, name of files to a log file

import os
import sys

fileName = os.path.basename(__file__)
rootDir = sys.argv[1]

print(fileName)
print(rootDir)