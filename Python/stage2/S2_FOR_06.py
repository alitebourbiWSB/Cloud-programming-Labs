# S2_FOR_06 — Sum nested arrays
def sum_nested(matrix):
   total = 0
   for row in matrix:
       for v in row:
           total += v
   return total
print(sum_nested([[1,2,3], [4,5], [6]]))