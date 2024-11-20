fruit = ['Apple', 'Pear', 'Orange']
print("Fruit:", fruit)

# this assigns the object reference to the new lunch variable
# both variables point to the same object in memory
lunch = fruit
print("Lunch:", lunch)

# change an item
lunch[1] = 'Eggs'
print("Fruit:", fruit)
print("Lunch:", lunch)
print("")
# Simple solution for simple sequences
# take a slice of the whole collection

# new fuit list without eggs
fruit = ['Apple', 'Pear', 'Orange']

snack = fruit[:]
snack[1] = 'Eggs'
print('fruit:', fruit, '\nsnack:', snack, '\n')

# doesn't work with deeper collections
fruit = ['knife', 'plate', ['Apple', 'Pear', 'Orange']]
lunch = fruit[:]
lunch[2][1] = 'Eggs'
print('fruit:', fruit, '\nlunch:', lunch, '\n')

# Solution: take a deepcopy

import copy

fruit = ['knife', 'plate', ['Apple', 'Pear', 'Orange']]
lunch = copy.deepcopy(fruit)
lunch[2][1] = 'Eggs'
print('fruit:', fruit, '\nlunch:', lunch)

