# S1_IF_01 — Even or odd
def is_even(n):
   if n % 2 == 0:
       return "even"
   else:
       return "odd"
# Tests
for x in [1, 2, 5, 10]:
   print(x, "is", is_even(x))