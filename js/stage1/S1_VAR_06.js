// S1_VAR_06 — NaN pitfalls
function classifyNumberLike(x) {
  if (Number.isNaN(x)) return "nan";
  if (typeof x === "number") return "number";
  return "not-a-number";
}
[NaN, 0, "0", "abc", undefined].forEach((v) =>
  console.log(v, "=>", classifyNumberLike(v))
);
