# S1_VAR_09 — NameError demo
try:
   print(not_defined_variable)
except NameError as e:
   print("Error:", e)