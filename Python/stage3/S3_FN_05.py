def at_least(min_val):
   return lambda x: x >= min_val
print(list(filter(at_least(10), [1, 5, 10, 20])))