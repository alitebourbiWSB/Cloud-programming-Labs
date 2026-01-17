# S3_PIPE_04.py

# S3_PIPE_04 — array processing pipeline

from typing import List

def filter_valid_numbers(strings: List[str]) -> List[str]:

    return [s for s in strings if s is not None and str(s).strip() != ""]

def to_numbers(strings: List[str]) -> List[float]:

    result = []

    for s in strings:

        try:

            # allow integers and floats

            n = float(s)

            result.append(n)

        except (ValueError, TypeError):

            # skip invalid

            pass

    return result

def double_numbers(nums: List[float]) -> List[float]:

    return [n * 2 for n in nums]

def sum_numbers(nums: List[float]) -> float:

    return sum(nums)

def process(strings: List[str]) -> float:

    step1 = filter_valid_numbers(strings)

    step2 = to_numbers(step1)

    step3 = double_numbers(step2)

    return sum_numbers(step3)

# Example usage

if __name__ == "__main__":

    data = ["1", "x", "2.5", " 3 ", "", None, "bad", "4"]

    print(process(data))  # (1 + 2.5 + 3 + 4) * 2 = (10.5) * 2 = 21.0
 