# filter returns an iterator

import glob
import os

pattern = 'C:/Code/Pycharm/*'

# used in a for loop
for directory_name in (filter(os.path.isdir, glob.iglob(pattern))):
    print(directory_name)

# used to produce a list
dirs = list(filter(os.path.isdir, glob.iglob(pattern)))
print(dirs)