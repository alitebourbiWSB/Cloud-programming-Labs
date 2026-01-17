# S1_VAR_08 — Big integers

big = 10 ** 100

print("Big int digits:", len(str(big)))

print("Type:", type(big).__name__)

big_float = float(big)

print("Float representation:", big_float)

# Python integers have arbitrary precision; floats lose precision.
 