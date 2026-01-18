# S3_PIPE_02 — compose: right-to-left function composition

def compose(*fns):

    def runner(x):

        for fn in reversed(fns):

            x = fn(x)

        return x

    return runner


# Tests

f = lambda x: x + 1

g = lambda x: x * 2

h = lambda x: x - 3

p = compose(f, g, h)

print(p(10))  # f(g(h(10))) = (10 - 3) * 2 + 1 = 15
 