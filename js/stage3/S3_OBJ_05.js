// S3_OBJ_05 — Invert
function invert(obj) {
  const result = {};
  for (const key in obj) {
    const value = obj[key];
    if (result[value]) {
      result[value].push(key);
    } else {
      result[value] = [key];
    }
  }
  return result;
}
// Test
console.log(invert({ a: 1, b: 2, c: 1 }));
