# generators can use the yield keyword to make the function a generator function
# or they can use round brackets instead of square brackets in a list comprehension to return a generator

import os
import glob


# generator using yield
def get_dir_with_yield(path):
    pattern = os.path.join(path, '*')
    for file in glob.iglob(pattern):
        if os.path.isdir(file):
            yield file


# generator without using yield - uses round brackets
def get_dir_without_yield(path):
    pattern = os.path.join(path, '*')
    return (file
            for file in glob.iglob(pattern)
            if os.path.isdir(file))


# list comprehension - uses square brackets
def get_dir_as_list_comprehension(path):
    pattern = os.path.join(path, '*')
    return [file
            for file in glob.iglob(pattern)
            if os.path.isdir(file)]


path = 'C:/Code'

# check type of return object
func1 = type(get_dir_with_yield(path))
print(func1)

func2 = type(get_dir_without_yield(path))
print(func2)

func3 = type(get_dir_as_list_comprehension(path))
print(func3)

# use the objects (2 x generator, 1 x list)
list_func1 = list(get_dir_with_yield(path))
print(list_func1)

list_func2 = list(get_dir_without_yield(path))
print(list_func2)

print(get_dir_as_list_comprehension(path))