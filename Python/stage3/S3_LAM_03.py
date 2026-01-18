# S3_LAM_03 — Closure factory with lambda

def make_adder(x):

    return lambda y: x + y


add10 = make_adder(10)

add3 = make_adder(3)

# Tests

print(add10(5))

print(add3(5))
 