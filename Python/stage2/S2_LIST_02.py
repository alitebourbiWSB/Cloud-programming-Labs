# S2_LIST_02 — Deduplicate without using set

def unique(values):

    result = []

    for v in values:

        if v not in result:

            result.append(v)

    return result


# Tests

print(unique([1, 2, 2, 3, 1, 4, 3]))
 