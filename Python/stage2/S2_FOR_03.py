# S2_FOR_03 — Sum until threshold
def sum_until(nums, threshold):
   total = 0
   for n in nums:
       if total + n > threshold:
           break
       total += n
   return total
print(sum_until([1, 2, 3, 4, 5], 7))