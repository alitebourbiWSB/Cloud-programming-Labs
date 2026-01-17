# S2_LIST_05 — Stats calculation

def stats(nums):

    if not nums:

        return None

    total = sum(nums)

    return {

        "min": min(nums),

        "max": max(nums),

        "avg": total / len(nums),

        "sum": total

    }


# Tests

print(stats([1, 2, 3, 4]))

print(stats([-5, 0, 5]))

print(stats([]))
 