import os
import glob

myset = {'booboo', 'yogi', 'care', 'fozzie'}


def do_ftp(machine):
    return "ftp to " + machine


# set comprehension
results = {do_ftp(m) for m in myset}
print("SET Comprehension", "*" * 50)
print(results)


pattern = 'C:/Code/Pycharm/*'

# list comprehension (of tuples)
tsizes = [(fname, os.path.getsize(fname))
         for fname in glob.iglob(pattern)]

print("LIST Comprehension", "*" * 50)
print(tsizes)

dsizes = {fname: size
          for fname, size in tsizes
          if size > 0}

print("Dictionary Comprehension", "*" * 50)
print(dsizes)
