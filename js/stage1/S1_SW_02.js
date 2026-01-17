// S1_SW_02 — Command router
function runCommand(cmd) {
  switch (cmd) {
    case "start":
      return "System starting";
    case "stop":
      return "System stopping";
    case "status":
      return "System status: OK";
    default:
      return "Unknown command";
  }
}
// Tests
["start", "status", "stop", "restart"].forEach((c) =>
  console.log(c, "=>", runCommand(c))
);
