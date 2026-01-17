# S2_FOR_02 — Find first even number

def find_first_even(nums):

    for n in nums:

        if isinstance(n, int) and n % 2 == 0:

            return n

    return None


# Tests

print(find_first_even([1, 3, 5, 8, 10]))

print(find_first_even([1, 3, 5]))
 