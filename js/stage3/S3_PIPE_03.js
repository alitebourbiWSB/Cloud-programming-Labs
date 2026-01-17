// S3_PIPE_03 — String normalization pipeline
const pipe =
  (...fns) =>
  (value) =>
    fns.reduce((acc, fn) => fn(acc), value);
const normalize = pipe(
  (s) => s.trim(),
  (s) => s.toLowerCase(),
  (s) => s.replace(/\s+/g, " ")
);
// Test
console.log(normalize("  HeLLo    WoRLd   "));
