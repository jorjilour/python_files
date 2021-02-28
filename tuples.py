''''
Tuples - immutable
'''

numbers = (1, 1, 2, 9, 3)

print(numbers[0])
print(numbers.count(1))
print(numbers.index(3, 0, len(numbers)))

### UNPACKING
coordinates = (1, 2, 3)
list_coordinates = [1, 2, 3]
x, y, z = coordinates
a, b, c = list_coordinates
