// S2_FOR_02 — Find first even
function findFirstEven(nums) {
  for (const n of nums) {
    if (n % 2 === 0) {
      return n;
    }
  }
  return null;
}
// Tests
console.log(findFirstEven([1, 3, 7, 4, 9]));
console.log(findFirstEven([1, 3, 5]));
