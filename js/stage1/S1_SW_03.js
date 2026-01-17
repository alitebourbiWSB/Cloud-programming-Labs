// S1_SW_03 — Simple calculator
function calc(a, op, b) {
  switch (op) {
    case "+":
      return a + b;
    case "-":
      return a - b;
    case "*":
      return a * b;
    case "/":
      return b === 0 ? null : a / b;
    default:
      return null;
  }
}
// Tests
console.log(calc(5, "+", 3)); // 8
console.log(calc(5, "-", 3)); // 2
console.log(calc(5, "*", 3)); // 15
console.log(calc(5, "/", 0)); // null
console.log(calc(5, "x", 3)); // null
