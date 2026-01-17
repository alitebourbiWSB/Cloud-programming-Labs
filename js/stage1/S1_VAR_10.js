// S1_VAR_10 — Mini debugger
function inspect(value) {
  return {
    type: typeof value,
    isArray: Array.isArray(value),
    isNull: value === null,
    isNaN: Number.isNaN(value),
  };
}
[null, undefined, 0, NaN, [], {}, "x", () => {}].forEach((v) =>
  console.log(inspect(v))
);
