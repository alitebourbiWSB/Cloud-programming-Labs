// S2_FOR_03 — Sum until threshold
function sumUntil(nums, threshold) {
  let sum = 0;
  for (const n of nums) {
    if (sum + n > threshold) break;
    sum += n;
  }
  return sum;
}
// Tests
console.log(sumUntil([1, 2, 3, 4, 5], 7));
console.log(sumUntil([5, 5, 5], 6));
