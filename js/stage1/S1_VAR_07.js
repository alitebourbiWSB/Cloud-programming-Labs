// S1_VAR_07 — Unary plus coercion
function toNumberOrNull(x) {
  if (typeof x !== "string") return null;
  const n = +x;
  return Number.isNaN(n) ? null : n;
}
["12", "12.5", " 12 ", "12x", ""].forEach((v) =>
  console.log(v, "=>", toNumberOrNull(v))
);
