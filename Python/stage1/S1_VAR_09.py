# S1_VAR_09 — Type hints

def add(a: int, b: int) -> int:

    return a + b

print(add(2, 3))

print(add("a", "b"))  # Works at runtime

# Type hints help tools, not runtime enforcement.
 