// S1_SW_01 — Day name
function dayName(n) {
  switch (n) {
    case 1:
      return "Monday";
    case 2:
      return "Tuesday";
    case 3:
      return "Wednesday";
    case 4:
      return "Thursday";
    case 5:
      return "Friday";
    case 6:
      return "Saturday";
    case 7:
      return "Sunday";
    default:
      return null;
  }
}
// Tests
[1, 3, 7, 0, 8].forEach((d) => console.log(d, "=>", dayName(d)));
