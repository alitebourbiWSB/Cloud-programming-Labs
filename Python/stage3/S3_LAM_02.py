# S3_LAM_02 — Sort list of dicts by key using lambda

people = [

    {"name": "Ali", "age": 28},

    {"name": "Sara", "age": 22},

    {"name": "Ola", "age": 25},

]

print("Before:", people)

sorted_people = sorted(people, key=lambda p: p["age"])

print("After:", sorted_people)
 