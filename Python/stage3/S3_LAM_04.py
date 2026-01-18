# S3_LAM_04 — Sum of squares of even numbers

from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))

print("Evens:", evens)

squares = list(map(lambda x: x * x, evens))

print("Squares:", squares)

total = reduce(lambda a, b: a + b, squares, 0)

print("Sum of squares:", total)
 