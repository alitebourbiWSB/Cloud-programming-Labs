# S3_LAM_06 — Map values in dictionary

def map_values(d, fn):

    return {k: fn(v) for k, v in d.items()}


data = {"a": 1, "b": 2, "c": 3}

print(map_values(data, lambda x: x * 10))
 