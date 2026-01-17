// S2_ARR_01 - Clean numbers
function cleanNumbers(arr) {
 return arr
   .map(x => +x)
   .filter(x => !Number.isNaN(x));
}
const input = [" 1 ", "x", "2"];
const output = cleanNumbers(input);
console.log("Input:", input);
console.log("Output:", output);
