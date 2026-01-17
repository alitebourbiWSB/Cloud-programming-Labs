# S1_VAR_10 — Mini inspector
def inspect(value):
   return {
       "type": type(value),
       "is_none": value is None,
       "is_list": isinstance(value, list),
       "is_bool": isinstance(value, bool),
   }
tests = [None, 0, True, [], {}, "hi"]
for t in tests:
   print(inspect(t))