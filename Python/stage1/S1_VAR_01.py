# S1_VAR_01 — Catalog of values and type()

def show(name, value):

    print(f"{name:10} | {value!r:20} | {type(value)} | {type(value).__name__}")

# Variables of different types

i = 10

f = 3.14

s = "hello"

b = True

n = None

lst = [1, 2, 3]

tup = (1, 2, 3)

dct = {"a": 1}

st = {1, 2, 3}

def fn():

    return "I am a function"

# Print table header

print(f"{'NAME':10} | {'VALUE':20} | TYPE | TYPE NAME")

print("-" * 70)

# Print values

show("int", i)

show("float", f)

show("str", s)

show("bool", b)

show("None", n)

show("list", lst)

show("tuple", tup)

show("dict", dct)

show("set", st)

show("function", fn)
 