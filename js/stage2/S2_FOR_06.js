// S2_FOR_06 — Nested arrays sum
function sumNested(matrix) {
  let sum = 0;
  for (const row of matrix) {
    for (const n of row) {
      sum += n;
    }
  }
  return sum;
}
// Test
console.log(sumNested([[1, 2], [3, 4], [5]]));
