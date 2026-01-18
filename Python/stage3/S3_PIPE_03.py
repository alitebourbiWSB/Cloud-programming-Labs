# S3_PIPE_03 — String normalization pipeline

import re

def pipe(*fns):

    def runner(x):

        for fn in fns:

            x = fn(x)

        return x

    return runner


normalize = pipe(

    lambda s: s.strip(),

    lambda s: s.lower(),

    lambda s: re.sub(r"\s+", " ", s),

)

print(normalize(" Ala   Ma    Kota "))
 