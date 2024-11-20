import os
import glob


def get_dir(path):
    pattern = os.path.join(path, '*')
    for file in glob.iglob(pattern):
        if os.path.isdir(file):
            yield file


# print a list of directories
for dir in get_dir('C:/Code'):
    print(dir)


print("\n")
# get a list of directories
dirs = list(get_dir('C:/Code'))
print(dirs)

# With generators and lazy lists, only the result immediately being processed is held.
