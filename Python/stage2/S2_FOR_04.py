# S2_FOR_04 — Count occurrences

def count_occurrences(values):

    counts = {}

    for v in values:

        if v in counts:

            counts[v] += 1

        else:

            counts[v] = 1

    return counts


# Tests

print(count_occurrences(["a", "b", "a", "c", "b", "a"]))
 