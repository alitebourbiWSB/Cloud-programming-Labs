# S3_PIPE_05 — Log processing pipeline

def parse_line(line):

    try:

        level, rest = line.split(":", 1)

        parts = rest.strip().split()

        data = {"level": level}

        for p in parts:

            k, v = p.split("=")

            data[k] = v

        return data

    except Exception:

        return None


lines = [

    "INFO: user=42 action=login",

    "DEBUG: user=10 action=ping",

    "INFO: user=7 action=logout",

    "INFO: action=broken",

]

parsed = (parse_line(l) for l in lines)

infos = (p for p in parsed if p and p.get("level") == "INFO")

user_ids = []

for item in infos:

    try:

        user_ids.append(int(item["user"]))

    except Exception:

        pass

print(user_ids)
 