# S2_ARR_01 — Clean numbers
def clean_numbers(values):
   result = []
   for v in values:
       try:
           n = float(v)
           result.append(n)
       except ValueError:
           pass
   return result
data = [" 1 ", "x", "2", " 3.5 ", "abc"]
print(clean_numbers(data))