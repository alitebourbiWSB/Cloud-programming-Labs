# S1_MC_02 — Command router using match/case

def run_command(cmd: str):

    match cmd:

        case "start":

            return "STARTING"

        case "stop":

            return "STOPPING"

        case "status":

            return "STATUS_OK"

        case _:

            return "UNKNOWN_COMMAND"


# Tests

commands = ["start", "stop", "status", "restart", "", None]

for c in commands:

    print(repr(c), "->", run_command(c))
 