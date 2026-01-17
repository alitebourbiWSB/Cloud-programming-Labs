# S3_OBJ_05 — Invert dictionary
def invert(obj):
   result = {}
   for k, v in obj.items():
       if v in result:
           if isinstance(result[v], list):
               result[v].append(k)
           else:
               result[v] = [result[v], k]
       else:
           result[v] = k
   return result
print(invert({"a": 1, "b": 2, "c": 1}))