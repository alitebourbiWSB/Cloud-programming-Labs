// S2_ARR_01 — Clean numbers
function cleanNumbers(arr) {
  return arr.map((v) => +v).filter((v) => !Number.isNaN(v));
}
// Test
const input = [" 1 ", "x", "2", "3.5", "abc"];
console.log(cleanNumbers(input)); // [1, 2, 3.5]
