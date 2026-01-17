// S3_OBJ_01 — Safe read
function get(obj, path, fallback) {
  const keys = path.split(".");
  let current = obj;
  for (const k of keys) {
    if (current == null || !(k in current)) {
      return fallback;
    }
    current = current[k];
  }
  return current;
}
// Tests
const data = { a: { b: { c: 42 } } };
console.log(get(data, "a.b.c", null));
console.log(get(data, "a.x.c", "missing"));
