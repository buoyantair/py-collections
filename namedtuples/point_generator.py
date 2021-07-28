from collections import namedtuple

# Use a generator expression as field names
Point = namedtuple('Point', (field for field in 'xy'))
print(Point(2, 4))
