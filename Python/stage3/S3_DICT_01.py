# S3_DICT_01 — Safe get by dotted path

def get_path(obj, path, fallback=None):

    current = obj

    for key in path.split("."):

        if not isinstance(current, dict) or key not in current:

            return fallback

        current = current[key]

    return current


# Tests

data = {"a": {"b": {"c": 42}}}

print(get_path(data, "a.b.c", None))

print(get_path(data, "a.b.x", "missing"))

print(get_path(data, "a.b.c.d", "missing"))
 