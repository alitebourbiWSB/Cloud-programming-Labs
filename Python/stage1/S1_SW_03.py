# S1_SW_03 — Simple calculator
def calc(a, op, b):
   match op:
       case "+":
           return a + b
       case "-":
           return a - b
       case "*":
           return a * b
       case "/":
           if b == 0:
               return None
           return a / b
       case _:
           return None
# Tests
tests = [
   (4, "+", 2),
   (4, "-", 2),
   (4, "*", 2),
   (4, "/", 2),
   (4, "/", 0),
]
for t in tests:
   print(t, "=>", calc(*t))