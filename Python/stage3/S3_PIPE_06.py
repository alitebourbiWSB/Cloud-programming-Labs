# S3_PIPE_06.py

# S3_PIPE_06 — safe pipeline

from typing import Callable, Any

def pipe_safe(*funcs: Callable[[Any], Any]) -> Callable[[Any], dict]:

    def run(value):

        try:

            for fn in funcs:

                value = fn(value)

            return {"ok": True, "value": value}

        except Exception as e:

            return {"ok": False, "error": str(e)}

    return run

# Example usage

if __name__ == "__main__":

    def inc(x): return x + 1

    def boom(x): raise RuntimeError("boom happened")

    safe1 = pipe_safe(inc, inc)

    safe2 = pipe_safe(inc, boom, inc)

    print(safe1(3))  # {'ok': True, 'value': 5}

    print(safe2(3))  # {'ok': False, 'error': 'boom happened'}
 