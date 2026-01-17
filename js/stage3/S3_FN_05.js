// S3_FN_05 — Higher-order predicate

const atLeast = (min) => (value) => value >= min;

// Test

const numbers = [1, 5, 10, 20];

console.log(numbers.filter(atLeast(10)));
