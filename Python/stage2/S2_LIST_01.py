# S2_LIST_01 — Clean number strings

def clean_numbers(values):

    result = []

    for v in values:

        try:

            result.append(float(v.strip()))

        except Exception:

            pass

    return result


# Tests

tests = [" 1 ", "x", "2", " 3.5 ", "", "  -4  "]

print(clean_numbers(tests))
 