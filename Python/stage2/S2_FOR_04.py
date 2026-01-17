# S2_FOR_04 — Count occurrences
def count_occurrences(values):
   result = {}
   for v in values:
       result[v] = result.get(v, 0) + 1
   return result
print(count_occurrences(["a", "b", "a", "c", "b", "a"]))