#Compare file names and file sizes of files inside an original directory with file names and file sizes inside a destination directory.
#Write name of script, discs, name of files to a log file

import os
import sys
import time

script_name = os.path.basename(__file__)
root_dir = sys.argv[1]
timestr = time.strftime("%Y_%d_%m-%H_%M")
log_file = timestr + '-' + os.path.splitext(script_name)[0] + '-log.txt'
dir_level = 0
print('Running ' + script_name + '...')

with open(log_file, 'wb') as log:
    for current_dir, subdirs, files in os.walk(root_dir):
        log.write(('\n--------------------------\n').encode('utf-8'))
        log.write((dir_level * '\t' + current_dir + '\n\n').encode('utf-8'))
        dir_level += 1
        for subdir in subdirs:
            log.write((dir_level * '\t' + '- Found subdirectory:\t' + subdir + '\n').encode('utf-8'))
        for file_name in files:
            log.write((dir_level * '\t' + '- Found file:\t\t' + file_name + '\n').encode('utf-8'))
                
print('Success. Logged results in ' + log_file)
