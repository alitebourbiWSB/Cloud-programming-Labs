# S2_LIST_06 — Transform records

def active_user_names(users):

    return sorted(

        [u["name"].upper() for u in users if u.get("active")]

    )


# Tests

users = [

    {"id": 1, "name": "Ali", "active": True},

    {"id": 2, "name": "Sara", "active": False},

    {"id": 3, "name": "Ola", "active": True},
 
 ]

print(active_user_names(users))
 