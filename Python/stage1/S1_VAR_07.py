# S1_VAR_07 — Safe int conversion
def to_int_or_none(x):
   try:
       return int(x)
   except (ValueError, TypeError):
       return None
tests = ["12", "12.5", "abc", None]
for t in tests:
   print(t, "=>", to_int_or_none(t))