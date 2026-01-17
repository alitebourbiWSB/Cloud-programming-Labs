# S2_ARR_02 — Deduplicate list
def unique(values):
   result = []
   for v in values:
       if v not in result:
           result.append(v)
   return result
print(unique([1, 2, 2, 3, 1, 4]))