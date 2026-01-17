// S3_PIPE_05 — Log lines pipeline
const pipe =
  (...fns) =>
  (value) =>
    fns.reduce((acc, fn) => fn(acc), value);
const logs = ["INFO: user=42", "ERROR: user=7", "INFO: user=99"];
const extractInfoUsers = pipe(
  (lines) => lines.filter((l) => l.startsWith("INFO")),
  (lines) => lines.map((l) => l.split("user=")[1])
);
// Test
console.log(extractInfoUsers(logs)); // ["42", "99"]
