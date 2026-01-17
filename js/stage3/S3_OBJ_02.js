// S3_OBJ_02 — Merge config
function mergeDefaults(defaults, overrides) {
  return { ...defaults, ...overrides };
}
// Test
console.log(mergeDefaults({ host: "localhost", port: 80 }, { port: 3000 }));
