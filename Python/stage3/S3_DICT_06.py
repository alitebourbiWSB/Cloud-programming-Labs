# S3_DICT_06 — Group by property

def group_by(items, key):

    groups = {}

    for item in items:

        if key not in item:

            continue

        value = item[key]

        groups.setdefault(value, []).append(item)

    return groups


# Tests

users = [

    {"name": "Ali", "role": "admin"},

    {"name": "Sara", "role": "user"},

    {"name": "Ola", "role": "admin"},

]

print(group_by(users, "role"))
 