# S1_VAR_04 — is vs ==

a = [1, 2]

b = [1, 2]

print(a == b)   # True (same value)

print(a is b)   # False (different objects)

x = None

print(x is None)  # Correct way to check None

# Use 'is' for identity, '==' for equality.
 