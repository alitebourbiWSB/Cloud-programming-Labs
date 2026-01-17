def make_adder(x):
   return lambda y: x + y
add5 = make_adder(5)
print(add5(10))