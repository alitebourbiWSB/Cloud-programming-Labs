# S3_PIPE_01.py

# S3_PIPE_01 — pipe()

from typing import Callable, Any

def pipe(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:

    def run(value):

        for fn in funcs:

            value = fn(value)

        return value

    return run

# Example usage / tests

if __name__ == "__main__":

    inc = lambda x: x + 1

    dbl = lambda x: x * 2

    p = pipe(inc, dbl, str)

    print(p(3))           # (3+1)*2 -> 8 -> "8"
 