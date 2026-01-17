def map_values(obj, fn):
   return {k: fn(v) for k, v in obj.items()}
print(map_values({"a": 1, "b": 2}, lambda v: v * 2))