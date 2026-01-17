// S3_FN_02 — Sort by property
const people = [
  { name: "Ali", age: 26 },
  { name: "Sara", age: 22 },
  { name: "John", age: 30 },
];
people.sort((a, b) => a.age - b.age);
console.log(people);
