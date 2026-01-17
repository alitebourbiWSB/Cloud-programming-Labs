// S1_VAR_03 — const is not immutable
const user = { name: "Ala", tags: [] };
user.tags.push("js");
user.tags.push("node");
console.log("After mutation:", user);
try {
  user = {};
} catch (err) {
  console.log("Reassignment error:", err.message);
}
