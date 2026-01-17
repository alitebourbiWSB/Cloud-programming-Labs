# S1_IF_01 — Shipping cost calculation

def shipping_cost(weight_kg, is_member):

    # Validate weight

    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:

        return None

    if weight_kg <= 1:

        cost = 10

    elif weight_kg <= 5:

        cost = 20

    else:

        cost = 30

    if is_member:

        cost *= 0.8  # 20% discount

    return cost


# Tests (including boundaries)

tests = [

    (0.5, False),

    (1, True),

    (3, False),

    (5, True),

    (6, False),

    (-1, True),

    ("5", False)

]

for w, m in tests:

    print(f"weight={w}, member={m} ->", shipping_cost(w, m))
 