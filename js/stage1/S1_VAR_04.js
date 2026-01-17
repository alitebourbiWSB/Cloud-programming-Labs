// S1_VAR_04 — Safe type label
function typeLabel(value) {
  return value === null ? "null" : typeof value;
}
const tests = [null, undefined, 42, "42", true, {}, [], () => {}];
tests.forEach((v) => {
  console.log(v, "=>", typeLabel(v));
});
