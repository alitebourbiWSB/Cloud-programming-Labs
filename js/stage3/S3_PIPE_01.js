// S3_PIPE_01 — pipe (left to right)
const pipe =
  (...fns) =>
  (value) =>
    fns.reduce((acc, fn) => fn(acc), value);
// Test
const add1 = (x) => x + 1;
const double = (x) => x * 2;
const fn = pipe(add1, double);
console.log(fn(3)); // (3 + 1) * 2 = 8
