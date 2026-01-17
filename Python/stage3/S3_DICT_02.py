# S3_DICT_02 — Merge defaults (shallow)

def merge_defaults(defaults, overrides):

    return {**defaults, **overrides}


# Tests

defaults = {"timeout": 10, "db": {"host": "localhost"}}

overrides = {"timeout": 5}

merged = merge_defaults(defaults, overrides)

print(merged)

# Shallow merge demonstration

merged["db"]["host"] = "remote"

print("defaults after shallow merge:", defaults)
 