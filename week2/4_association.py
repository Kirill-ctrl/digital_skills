from functools import reduce

print(reduce(lambda x, y: (x + ' ' + y).lower(), ['privet', 'mir', 'hello', 'world']))
