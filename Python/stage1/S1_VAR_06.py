# S1_VAR_06 — Safe int conversion

def to_int_or_none(s):

    try:

        return int(s)

    except Exception:

        return None

tests = ["12", " 12 ", "12x", "", None]

for t in tests:

    print(repr(t), "=>", to_int_or_none(t))
 