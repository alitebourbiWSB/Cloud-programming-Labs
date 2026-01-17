// S3_PIPE_02 — compose (right to left)
const compose =
  (...fns) =>
  (value) =>
    fns.reduceRight((acc, fn) => fn(acc), value);
// Test
const add1 = (x) => x + 1;
const double = (x) => x * 2;
const fn = compose(add1, double);
console.log(fn(3)); // add1(double(3)) = 7
