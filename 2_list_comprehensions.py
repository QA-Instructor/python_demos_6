# A list comprehension returns a list.
# It consists of:
# A loop - typically a for loop.
# An expression which identifies a list item.
# An optional condition to filter items.
import os
import glob

pattern = 'C:/Code/Pycharm/*'

# get a list of file sizes
sizes = [os.path.getsize(name) for name in glob.iglob(pattern)]
print(sizes)

# get a list of file sizes greater than 0
sizes = [os.path.getsize(name) for name in glob.iglob(pattern) if os.path.getsize(name) > 0]
print(sizes)

# get a list of directories
dirs = [dirname for dirname in glob.iglob(pattern) if os.path.isdir(dirname)]
print(dirs)
