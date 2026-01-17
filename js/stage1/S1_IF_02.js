// S1_IF_02 — Score to grade
function grade(score) {
  if (score < 0 || score > 100) return null;
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}
// Tests
[95, 82, 74, 61, 40, -1, 120].forEach((s) => console.log(s, "=>", grade(s)));
