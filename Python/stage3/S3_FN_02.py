people = [
   {"name": "Ali", "age": 26},
   {"name": "Sara", "age": 22},
   {"name": "John", "age": 30},
]
people.sort(key=lambda p: p["age"])
print(people)