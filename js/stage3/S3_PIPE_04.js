// S3_PIPE_04 — Array processing pipeline
const pipe =
  (...fns) =>
  (value) =>
    fns.reduce((acc, fn) => fn(acc), value);
const processNumbers = pipe(
  (arr) => arr.map((x) => +x).filter((x) => !Number.isNaN(x)),
  (arr) => arr.map((x) => x * 2),
  (arr) => arr.reduce((a, b) => a + b, 0)
);
// Test
console.log(processNumbers(["1", "x", "2", "3"])); // (1+2+3)*2 = 12
