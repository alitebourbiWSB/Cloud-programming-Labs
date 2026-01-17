# S1_VAR_03 — Mutability

lst = [1, 2, 3]

lst[0] = 99

print("List:", lst)

tup = (1, 2, 3)

try:

    tup[0] = 99

except Exception as e:

    print("Tuple error:", e)

# Lists are mutable; tuples are immutable.
 