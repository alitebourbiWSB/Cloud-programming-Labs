// S1_VAR_08 — Big integers
function safeAdd(a, b) {
  if (
    Number.isInteger(a) &&
    Number.isInteger(b) &&
    (Math.abs(a) > Number.MAX_SAFE_INTEGER ||
      Math.abs(b) > Number.MAX_SAFE_INTEGER)
  ) {
    const result = BigInt(a) + BigInt(b);
    console.log("BigInt result:", result, typeof result);
    return result;
  }
  const result = a + b;
  console.log("Number result:", result, typeof result);
  return result;
}
safeAdd(1, 2);
safeAdd(Number.MAX_SAFE_INTEGER + 1, 1);
