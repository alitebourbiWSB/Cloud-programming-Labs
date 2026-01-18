# S3_LAM_05 — Higher-order predicate

def at_least(min_value):

    return lambda x: x >= min_value


nums = [1, 3, 5, 7, 10]

filtered = list(filter(at_least(5), nums))

print(filtered)
 