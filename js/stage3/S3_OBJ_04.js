// S3_OBJ_04 — Omit
function omit(obj, keys) {
  const result = {};
  for (const k in obj) {
    if (!keys.includes(k)) {
      result[k] = obj[k];
    }
  }
  return result;
}
// Test
console.log(omit({ a: 1, b: 2, c: 3 }, ["b"]));
