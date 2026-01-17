// S2_ARR_06 — Transform records
const users = [
  { id: 1, name: "ola", active: true },
  { id: 2, name: "adam", active: false },
  { id: 3, name: "ewa", active: true },
];
const result = users
  .filter((u) => u.active)
  .map((u) => u.name.toUpperCase())
  .sort();
console.log(result);
