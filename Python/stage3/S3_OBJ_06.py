# S3_OBJ_06 — Group by key
def group_by(items, key):
   result = {}
   for item in items:
       k = item.get(key)
       result.setdefault(k, []).append(item)
   return result
items = [
   {"type": "a", "value": 1},
   {"type": "b", "value": 2},
   {"type": "a", "value": 3},
]
print(group_by(items, "type"))