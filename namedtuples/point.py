from collections import namedtuple

# Use a list of strings as field names to build a Point namedtuple.

Point = namedtuple('Point', ['x', 'y'])
point = Point(2, 4)
print(point)

