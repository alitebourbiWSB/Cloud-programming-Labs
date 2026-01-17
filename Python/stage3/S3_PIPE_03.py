# S3_PIPE_03.py

# S3_PIPE_03 — string normalization

import re

from typing import Callable

def trim(s: str) -> str:

    return s.strip()

def lower(s: str) -> str:

    return s.lower()

def collapse_spaces(s: str) -> str:

    return re.sub(r'\s+', ' ', s)

def make_normalizer() -> Callable[[str], str]:

    # left-to-right pipeline

    def run(s: str) -> str:

        return collapse_spaces(lower(trim(s)))

    return run

# Example usage

if __name__ == "__main__":

    normalize = make_normalizer()

    print(normalize("  HeLLo    WORLD  "))  # "hello world"

    print(normalize("\n  MULTI\tspace \t test  "))  # "multi space test"
 