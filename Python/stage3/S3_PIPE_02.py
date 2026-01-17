# S3_PIPE_02.py

# S3_PIPE_02 — compose()

from typing import Callable, Any

def compose(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:

    def run(value):

        for fn in reversed(funcs):

            value = fn(value)

        return value

    return run

# Example usage / tests

if __name__ == "__main__":

    inc = lambda x: x + 1

    dbl = lambda x: x * 2

    c = compose(str, dbl, inc)  # str(dbl(inc(x)))

    print(c(3))  # inc(3)=4 -> dbl=8 -> "8"
 