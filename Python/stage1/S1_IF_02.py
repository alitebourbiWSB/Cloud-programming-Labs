# S1_IF_02 — Score to grade
def grade(score):
   if score < 0 or score > 100:
       return None
   elif score >= 90:
       return "A"
   elif score >= 80:
       return "B"
   elif score >= 70:
       return "C"
   elif score >= 60:
       return "D"
   else:
       return "F"
# Tests
for s in [95, 82, 74, 61, 40, -5]:
   print(s, "=>", grade(s))