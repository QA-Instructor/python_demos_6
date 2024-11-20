# Lazy lists are implemented by supplying an iterator (position) to a list, rather than the whole list itself
# Generator functions are a special kind of function that return a lazy iterator.
# These are objects that you can loop over like a list.
# Unlike lists, lazy iterators do not store their contents in memory.

# YIELD makes a function a generator function

# Example: imagine we have a very large file with millions of rows
# def csv_reader(file_name):
#     for row in (file_name, "r"):
#         yield row

# Yield expressions and statements are only used when defining a generator function, and are only used in the
# body of the generator function. Using yield in a function definition is sufficient to cause that
# definition to create a generator function instead of a normal function

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


print("========== Example 1 ==========")
# for i in infinite_sequence():
#     print(i, end=" ")

# Ctrl + F12 or red stop button to stop the infinite sequence


print("========== Example 2 ==========")
gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


