// S3_PIPE_06 — Safe pipeline
const pipeSafe =
  (...fns) =>
  (value) => {
    try {
      let result = value;
      for (const fn of fns) {
        result = fn(result);
      }
      return { ok: true, value: result };
    } catch (error) {
      return { ok: false, error: error.message };
    }
  };
// Tests
const safeFn = pipeSafe(
  (x) => x + 1,
  (x) => {
    if (x > 3) throw new Error("Too big");
    return x;
  }
);
console.log(safeFn(1)); // ok
console.log(safeFn(5)); // error
