# S3_OBJ_02 — Merge config (shallow)
def merge_defaults(defaults, overrides):
   result = defaults.copy()
   result.update(overrides)
   return result
print(merge_defaults(
   {"host": "localhost", "port": 80},
   {"port": 8080}
))