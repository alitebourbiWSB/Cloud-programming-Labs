# S3_OBJ_01 — Safe read
def get(obj, path, fallback=None):
   current = obj
   for key in path.split("."):
       if isinstance(current, dict) and key in current:
           current = current[key]
       else:
           return fallback
   return current
data = {"a": {"b": {"c": 42}}}
print(get(data, "a.b.c"))
print(get(data, "a.b.x", "missing"))