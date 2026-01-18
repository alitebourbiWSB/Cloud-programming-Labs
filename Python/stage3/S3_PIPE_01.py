# S3_PIPE_01 — pipe: left-to-right function composition

def pipe(*fns):

    def runner(x):

        for fn in fns:

            x = fn(x)

        return x

    return runner


# Tests

f = lambda x: x + 1

g = lambda x: x * 2

h = lambda x: x - 3

p = pipe(f, g, h)

print(p(10))  # ((10 + 1) * 2) - 3 = 19
 