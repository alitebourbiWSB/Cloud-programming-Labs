# S2_LIST_04 — Flatten one level

def flatten1(lst):

    result = []

    for item in lst:

        if isinstance(item, list):

            for x in item:

                result.append(x)

        else:

            result.append(item)

    return result


# Tests

print(flatten1([1, [2, 3], [4], 5]))
 