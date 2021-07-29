from collections import namedtuple

def custom_divmod(x, y):
  DivMod = namedtuple('DivMod', ['quotient', 'remainder'])
  return DivMod(*divmod(x, y))

result = custom_divmod(7, 3)
print(result)
