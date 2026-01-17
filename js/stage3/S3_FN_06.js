// S3_FN_06 — Map values
const mapValues = (obj, fn) => {
  const result = {};
  for (const key in obj) {
    result[key] = fn(obj[key]);
  }
  return result;
};
// Test
console.log(mapValues({ a: 1, b: 2, c: 3 }, (x) => x * 2));
