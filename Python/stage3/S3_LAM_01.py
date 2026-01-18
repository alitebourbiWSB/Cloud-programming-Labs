# S3_LAM_01 — Convert functions to lambdas

square = lambda n: n * n

is_odd = lambda n: n % 2 == 1

greet = lambda name: f"Hello, {name}"

# Tests

print(square(2), square(5), square(10))

print(is_odd(1), is_odd(2), is_odd(7))

print(greet("Ali"), greet("Ola"), greet("Sara"))
 