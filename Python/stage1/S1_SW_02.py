# S1_SW_02 — Command router
def run_command(cmd):
   match cmd:
       case "start":
           return "System starting"
       case "stop":
           return "System stopping"
       case "status":
           return "System status: OK"
       case _:
           return "Unknown command"
# Tests
commands = ["start", "stop", "status", "restart"]
for c in commands:
   print(c, "=>", run_command(c))