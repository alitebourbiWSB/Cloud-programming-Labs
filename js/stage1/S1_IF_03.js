// S1_IF_03 — Truthy/falsy guard
function normalizeName(input) {
  if (!input) return "Anonymous";
  return input.trim() || "Anonymous";
}
// Tests
["", " ", null, " Ola "].forEach((v) =>
  console.log(JSON.stringify(v), "=>", normalizeName(v))
);
