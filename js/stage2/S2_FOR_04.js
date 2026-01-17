// S2_FOR_04 — Count occurrences
function countOccurrences(values) {
  const result = {};
  for (const v of values) {
    result[v] = (result[v] || 0) + 1;
  }
  return result;
}
// Test
console.log(countOccurrences(["a", "b", "a", "c", "b", "a"]));
