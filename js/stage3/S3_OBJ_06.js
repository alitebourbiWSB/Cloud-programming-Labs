// S3_OBJ_06 — Group by
function groupBy(items, key) {
  const result = {};
  for (const item of items) {
    const value = item[key];
    if (!result[value]) result[value] = [];
    result[value].push(item);
  }
  return result;
}
// Test
console.log(
  groupBy(
    [
      { name: "A", type: "x" },
      { name: "B", type: "y" },
      { name: "C", type: "x" },
    ],
    "type"
  )
);
