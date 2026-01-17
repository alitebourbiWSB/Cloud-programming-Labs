# S2_ARR_06 — Transform records
users = [
   {"id": 1, "name": "ola", "active": True},
   {"id": 2, "name": "jan", "active": False},
   {"id": 3, "name": "anna", "active": True},
]
def active_user_names(users):
   names = []
   for u in users:
       if u["active"]:
           names.append(u["name"].upper())
   return sorted(names)
print(active_user_names(users))