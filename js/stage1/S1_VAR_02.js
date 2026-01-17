// S1_VAR_02 - Block scope check

try {

  {

    let x = 10;

  }

  console.log(x);

} catch (e) {

  console.log("let is block-scoped and not accessible outside");

}

try {

  {

    var y = 20;

  }

  console.log("var value outside block:", y);

} catch (e) {

  console.log("This will not happen for var");

}

// Explanation:

// let is block-scoped, var is function-scoped
 
