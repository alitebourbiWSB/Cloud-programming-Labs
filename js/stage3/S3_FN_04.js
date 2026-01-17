// S3_FN_04 — Sum of squares of even numbers
const nums = [1, 2, 3, 4, 5, 6];
const result = nums
  .filter((n) => n % 2 === 0)
  .map((n) => n * n)
  .reduce((a, b) => a + b, 0);
console.log(result);
