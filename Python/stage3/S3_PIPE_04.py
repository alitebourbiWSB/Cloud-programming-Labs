# S3_PIPE_04 — Generator-based numeric pipeline

def to_floats(values):

    for v in values:

        try:

            yield float(v.strip())

        except Exception:

            continue


values = [" 1 ", "x", "2.5", " 3 ", "bad"]

numbers = to_floats(values)

doubled = (n * 2 for n in numbers)

total = sum(doubled)

print(total)
 