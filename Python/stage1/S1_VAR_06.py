# S1_VAR_06 — Truthy / falsy
tests = [0, 1, "", "text", None, [], [1]]
for t in tests:
   print(repr(t), "=>", bool(t))