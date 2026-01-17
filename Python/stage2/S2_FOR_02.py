# S2_FOR_02 — Find first even
def find_first_even(nums):
   for n in nums:
       if n % 2 == 0:
           return n
   return None
print(find_first_even([1, 3, 5, 8, 9]))
print(find_first_even([1, 3, 5]))