# S1_VAR_04 — Type inspection
values = [None, 42, 3.14, "42", True, [], {}, lambda x: x]
for v in values:
   print(v, "=>", type(v))