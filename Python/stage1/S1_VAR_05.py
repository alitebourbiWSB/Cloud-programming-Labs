# S1_VAR_05 — List vs tuple
lst = [1, 2, 3]
tpl = (1, 2, 3)
lst.append(4)
print("List:", lst)
try:
   tpl.append(4)
except AttributeError as e:
   print("Tuple error:", e)