# S3_OBJ_03 — Pick keys
def pick(obj, keys):
   return {k: obj[k] for k in keys if k in obj}
print(pick({"a": 1, "b": 2, "c": 3}, ["a", "c"]))