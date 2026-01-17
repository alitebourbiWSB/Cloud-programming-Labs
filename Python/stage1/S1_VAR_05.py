# S1_VAR_05 — Truthiness

def is_truthy(v):

    return bool(v)

tests = [0, 1, "", "0", [], [0], {}, None]

for t in tests:

    print(repr(t), "=>", is_truthy(t))
 