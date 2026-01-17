# S2_ARR_03 — Chunk list
def chunk(arr, size):
   if size <= 0:
       return None
   result = []
   for i in range(0, len(arr), size):
       result.append(arr[i:i+size])
   return result
print(chunk([1,2,3,4,5,6,7], 3))