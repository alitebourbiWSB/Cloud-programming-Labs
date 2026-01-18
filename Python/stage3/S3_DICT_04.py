# S3_DICT_04 — Omit keys from dict

def omit(d, keys):

    return {k: v for k, v in d.items() if k not in keys}


# Tests

data = {"a": 1, "b": 2, "c": 3}

print(omit(data, ["b"]))
 