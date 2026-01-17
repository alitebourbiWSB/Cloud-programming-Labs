// S1_VAR_02 — Block scope check
try {
  {
    let x = 10;
    console.log("Inside block (let):", x);
  }
  console.log(x); // ReferenceError
} catch (err) {
  console.log("let is block-scoped: x is not accessible outside the block");
}
{
  var y = 20;
  console.log("Inside block (var):", y);
}
console.log("Outside block (var):", y);
// Explanation:
// let is block-scoped, so it exists only inside {}.
// var is function-scoped, so it leaks outside the block.
