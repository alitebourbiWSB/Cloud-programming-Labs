# S1_IF_03 — Falsy guard
def normalize_name(value):
   if not value:
       return "Anonymous"
   return value.strip()
# Tests
tests = ["", " ", None, " Ola "]
for t in tests:
   print(repr(t), "=>", normalize_name(t))