# S2_ARR_04 — Flatten one level
def flatten1(arr):
   result = []
   for item in arr:
       if isinstance(item, list):
           result.extend(item)
       else:
           result.append(item)
   return result
print(flatten1([1, [2,3], [4], 5]))