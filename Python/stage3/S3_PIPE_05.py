# S3_PIPE_05.py

# S3_PIPE_05 — log lines pipeline

from typing import List, Dict, Optional

def parse_line(line: str) -> Optional[Dict[str, str]]:

    # Very simple parser: "LEVEL: key1=val1 key2=val2" or "LEVEL: key=val"

    if ":" not in line:

        return None

    level, rest = line.split(":", 1)

    level = level.strip()

    rest = rest.strip()

    # parse key=value pairs (space-separated)

    data = {}

    for part in rest.split():

        if "=" in part:

            k, v = part.split("=", 1)

            data[k.strip()] = v.strip()

    return {"level": level, **data}

def filter_info(parsed: Optional[Dict[str, str]]) -> bool:

    return parsed is not None and parsed.get("level") == "INFO"

def extract_user_id(parsed: Dict[str, str]) -> Optional[int]:

    uid = parsed.get("user")

    if uid is None:

        return None

    try:

        return int(uid)

    except (ValueError, TypeError):

        return None

def process_log_lines(lines: List[str]) -> List[int]:

    parsed = [parse_line(l) for l in lines]

    infos = [p for p in parsed if filter_info(p)]

    ids = [extract_user_id(p) for p in infos]

    return [i for i in ids if i is not None]

# Example usage

if __name__ == "__main__":

    lines = [

        "INFO: user=42 action=login",

        "ERROR: code=500",

        "INFO: user=7",

        "DEBUG: user=100",

        "INFO: user=bad"

    ]

    print(process_log_lines(lines))  # [42, 7]
 