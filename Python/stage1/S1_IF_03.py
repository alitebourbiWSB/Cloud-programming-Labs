# S1_IF_03 — Normalize user name

def normalize_name(x):

    if not x:

        return "Anonymous"

    name = x.strip()

    if name == "":

        return "Anonymous"

    return name


# Tests

tests = ["", " ", None, " Ola "]

for t in tests:

    print(f"input={repr(t)} ->", normalize_name(t))
 