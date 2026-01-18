# S3_PIPE_06 — Safe pipeline with error handling

def pipe_safe(*fns):

    def runner(x):

        try:

            for fn in fns:

                x = fn(x)

            return {"ok": True, "value": x}

        except Exception as e:

            return {"ok": False, "error": str(e)}

    return runner


# Functions

def to_int(x):

    return int(x)

def invert(x):

    return 1 / x


safe_pipeline = pipe_safe(to_int, invert)

print(safe_pipeline("5"))

print(safe_pipeline("0"))

print(safe_pipeline("abc"))
 